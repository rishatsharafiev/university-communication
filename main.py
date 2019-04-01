import asyncio
import logging
import logging.config

from aiohttp import web
from src import settings
from src.application import init_app


def app_factory():
    """Application factory"""
    # Initialize logging config
    logging.config.dictConfig(settings.LOGGING)

    # Get loop
    loop = asyncio.get_event_loop()

    # Run application
    app = loop.run_until_complete(init_app(loop))
    web.run_app(app, host=settings.APP_HOST, port=settings.APP_PORT)


if __name__ == '__main__':
    app_factory()
