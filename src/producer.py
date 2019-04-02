from aiohttp import web
from aiokafka import AIOKafkaProducer
from src import settings


async def producer_handler(request):
    """Producer handler"""
    producer = AIOKafkaProducer(loop=settings.loop, bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS)

    message = await request.json()

    await producer.start()
    try:
        print(message)
        await producer.send_and_wait(settings.KAFKA_TOPIC_SUCCESS, b"Super message")
    finally:
        await producer.stop()

    return web.Response(text='ok')
