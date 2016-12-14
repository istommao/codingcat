"""demo."""
from sanic import Sanic
from sanic.response import text

from server.urls import API_LIST

from extensions.routers import create_routers


def run_app(app_name):
    """run app."""
    app = Sanic(app_name)

    create_routers(app, API_LIST)

    @app.middleware('response')
    async def halt_response(request, response):
        ALLOW_METHODS = 'HEAD, POST, GET, PUT, DELETE, OPTIONS'
        ALLOW_HEADERS = 'Content-Type, x-requested-with'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Headers'] = ALLOW_HEADERS
        response.headers['Access-Control-Allow-Methods'] = ALLOW_METHODS
        return response

    app.run(host='127.0.0.1', port=8005, debug=True)

    return app


if __name__ == '__main__':
    run_app('codingcat')
