from aiohttp import web

from . import __version__


class RestVersion(web.View):
    async def get(self):
        return web.Response(text=__version__)
