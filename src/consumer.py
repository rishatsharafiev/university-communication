import json

import aiohttp
from aiokafka import AIOKafkaConsumer
from src import settings


async def consume_handler():
    """Consume handler"""
    consumer = AIOKafkaConsumer(
        settings.KAFKA_TOPIC_DOWNLOAD,
        loop=settings.loop, bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS)

    await consumer.start()
    try:
        # Consume messages
        async for msg in consumer:
            if msg.topic == settings.KAFKA_TOPIC_DOWNLOAD:
                try:
                    message = json.loads(msg.value)

                    # {"action": "download", "source": "application1", "url": "https://bit.ly/2F5nCiI"}
                    if 'action' in message and message.get('action') == 'download' \
                            and 'source' in message and 'url' in message:
                        timeout = aiohttp.ClientTimeout(total=5)
                        async with aiohttp.ClientSession(timeout=timeout) as session:
                            await session.post(settings.WEBHOOK_URL, json=message)
                except json.decoder.JSONDecodeError:
                    pass
    finally:
        # Will leave consumer group; perform autocommit if enabled.
        await consumer.stop()
