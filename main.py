import logging
import logging.config

from aiohttp import web
from src import settings
from src.application import init_app
from src.consumer import consume_handler


async def start_background_tasks(app):
    """On start"""
    app['consume_handler'] = app.loop.create_task(consume_handler())


async def cleanup_background_tasks(app):
    """On cleanup"""
    app['consume_handler'].cancel()
    await app['consume_handler']


def app_factory():
    """Application factory"""
    # Initialize logging config
    logging.config.dictConfig(settings.LOGGING)

    # Get loop
    loop = settings.loop

    # Run application
    app = loop.run_until_complete(init_app(loop))

    # Setup consumer
    app.on_startup.append(start_background_tasks)
    app.on_cleanup.append(cleanup_background_tasks)

    web.run_app(app, host=settings.APP_HOST, port=settings.APP_PORT)


if __name__ == '__main__':
    app_factory()
