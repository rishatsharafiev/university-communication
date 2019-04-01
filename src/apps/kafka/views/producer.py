from aiohttp import web


class ProducerView(web.View):
    """Producer View Class"""

    async def post(self):
        """Post method"""
        return web.Response(text=f'ok')
