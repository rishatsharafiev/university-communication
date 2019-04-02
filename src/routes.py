from aiohttp import web

from .producer import producer_handler


def setup_routes(app):
    """Setup application routes"""
    app.add_routes([
        web.post('/producer', producer_handler)
    ])
