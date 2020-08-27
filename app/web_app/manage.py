import os
import socket

from aiohttp import web

from .routes import setup_routes


def init_app():
    app = web.Application()

    setup_routes(app)

    return app


def run():
    app = init_app()
    web.run_app(
        app=app,
        path=os.environ.get('HOST'),
        port=os.environ.get('PORT')
    )
