import aiohttp
from aiohttp import web


async def get_version(request):
    message = f'{aiohttp.__name__}: {aiohttp.__version__}'
    return web.Response(text=message)


app = web.Application()
app.router.add_get('/stat', get_version)
web.run_app(app, port=8080)
