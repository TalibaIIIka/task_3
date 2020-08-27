from aiohttp import web

from .views import RestVersion


def setup_routes(app: web.Application):
    app.router.add_view('/stat', RestVersion, name='version')
