
DEBUG = False

APP_CONFIG = dict(
    host='127.0.0.1', port=8005, workers=2, debug=DEBUG
)

try:
    # pylint: disable=W0614, C0413, wildcard-import
    from server.local_settings import *   # noqa
except ImportError:
    pass
