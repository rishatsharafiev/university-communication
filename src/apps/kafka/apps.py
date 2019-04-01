from aiohttp import web

from .routes import routes

kafka_app = web.Application()
kafka_app.add_routes(routes)
