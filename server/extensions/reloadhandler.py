import os

import sys
import subprocess
import signal

import time
import threading

from itertools import chain

from sanic.log import log

try:
    import uvloop as async_loop
except ImportError:
    async_loop = asyncio


PY2 = sys.version_info[0] == 2


def _iter_module_files():
    """This iterates over all relevant Python files.  It goes through all
    loaded files from modules, all files in folders of already loaded modules
    as well as all files reachable through a package.
    """
    # The list call is necessary on Python 3 in case the module
    # dictionary modifies during iteration.
    for module in list(sys.modules.values()):
        if module is None:
            continue
        filename = getattr(module, '__file__', None)
        if filename:
            old = None
            while not os.path.isfile(filename):
                old = filename
                filename = os.path.dirname(filename)
                if filename == old:
                    break
            else:
                if filename[-4:] in ('.pyc', '.pyo'):
                    filename = filename[:-1]
                yield filename


class StatReloaderLoop(object):
    name = 'stat'

    # monkeypatched by testsuite. wrapping with `staticmethod` is required in
    # case time.sleep has been replaced by a non-c function (e.g. by
    # `eventlet.monkey_patch`) before we get here
    _sleep = staticmethod(time.sleep)

    def __init__(self, extra_files=None, interval=1, **kwargs):
        self.app = kwargs.pop('app')
        self.event_loop = kwargs.pop('event_loop')

        self.extra_files = set(os.path.abspath(x) for x in extra_files or ())
        self.interval = interval

    def run(self):
        mtimes = {}
        while 1:
            for filename in chain(_iter_module_files(), self.extra_files):
                try:
                    mtime = os.stat(filename).st_mtime
                except OSError:
                    continue

                old_time = mtimes.get(filename)
                if old_time is None:
                    mtimes[filename] = mtime
                    continue
                elif mtime > old_time:
                    self.trigger_reload(filename)
            self._sleep(self.interval)

    def restart_with_reloader(self):
        """Spawn a new Python interpreter with the same arguments as this one,
        but running the reloader thread.
        """
        text_type = unicode if PY2 else str

        while 1:
            log.info(' * Restarting with %s' % self.name)
            args = [sys.executable] + sys.argv
            new_environ = os.environ.copy()
            new_environ['WERKZEUG_RUN_MAIN'] = 'true'

            # a weird bug on windows. sometimes unicode strings end up in the
            # environment and subprocess.call does not like this, encode them
            # to latin1 and continue.
            if os.name == 'nt' and PY2:
                for key, value in new_environ.items():
                    if isinstance(value, text_type):
                        new_environ[key] = value.encode('iso-8859-1')

            exit_code = subprocess.call(args, env=new_environ, close_fds=False)
            if exit_code != 3:
                return exit_code

    def trigger_reload(self, filename):
        """Trigger reload."""
        self.event_loop.call_soon_threadsafe(self._stop_app)

        self.log_reload(filename)
        sys.exit(3)

    def log_reload(self, filename):
        """Log reload."""
        filename = os.path.abspath(filename)
        log.info(' * Detected change in %r, reloading' % filename)

    def _stop_app(self):
        self.app.stop()


def start_reloader_thread(event_loop, extra_files=None, interval=1, app=None):
    """Start reloader thread."""
    signal.signal(signal.SIGTERM, lambda *args: sys.exit(0))

    reloader = StatReloaderLoop(extra_files, interval, app=app,
                                event_loop=event_loop)

    thread = threading.Thread(target=reloader.run, args=())
    thread.setDaemon(True)
    thread.start()


def run_app(app, host='127.0.0.1', port=8005, debug=False):
    event_loop = async_loop.new_event_loop()

    # Run reloader thread
    start_reloader_thread(event_loop=event_loop, interval=1, app=app)

    app.run(host=host, port=port, loop=event_loop, debug=debug)

    args = [sys.executable] + sys.argv

    env_copy = os.environ.copy()

    subprocess.call(args, env=env_copy, close_fds=False)
