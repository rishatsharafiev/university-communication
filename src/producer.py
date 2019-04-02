import json

from aiohttp import web
from aiokafka import AIOKafkaProducer
from src import settings


async def producer_handler(request):
    """Producer handler"""
    producer = AIOKafkaProducer(loop=settings.loop, bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS)
    await producer.start()
    try:
        message = await request.json()

        if 'url' in message and 'source' in message:
            body = json.dumps(message).encode('utf-8')
            await producer.send_and_wait(settings.KAFKA_TOPIC_SUCCESS, body)
    except json.decoder.JSONDecodeError:
        pass
    finally:
        await producer.stop()

    return web.Response(text='ok')
