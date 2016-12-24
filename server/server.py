"""demo."""
import os

from sanic import Sanic

from server.urls import API_LIST

from extensions.routers import create_routers

from server.settings import APP_CONFIG


def create_app():
    """run app."""
    app = Sanic()

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    dist_path = '{}/web/dist/'.format(BASE_DIR)
    app.static('/dist', dist_path)

    create_routers(app, API_LIST)

    @app.middleware('response')
    async def halt_response(request, response):
        ALLOW_METHODS = 'HEAD, POST, GET, PUT, DELETE, OPTIONS'
        ALLOW_HEADERS = 'Content-Type, x-requested-with'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Headers'] = ALLOW_HEADERS
        response.headers['Access-Control-Allow-Methods'] = ALLOW_METHODS

        return response

    return app


def main():
    app = create_app()
    app.run(**APP_CONFIG)


if __name__ == '__main__':
    exit(main())
