"""demo."""
from sanic import Sanic

from server.urls import API_LIST

from extensions.routers import create_routers


def run_app(app_name):
    """run app."""
    app = Sanic(app_name)

    create_routers(app, API_LIST)

    app.run(host='127.0.0.1', port=8000)

    return app


if __name__ == '__main__':
    run_app('codingcat')
