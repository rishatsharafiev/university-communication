from aiohttp import web
from src.routes import setup_routes


async def init_app(loop=None):
    """Initialize application"""
    app = web.Application(
        middlewares=[],
        loop=loop
    )

    # Setup routes
    setup_routes(app)

    return app
