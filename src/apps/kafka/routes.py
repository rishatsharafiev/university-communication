from aiohttp import web

from .views import ProducerView

routes = [
    web.view('/producer', ProducerView, name='producer')
]
