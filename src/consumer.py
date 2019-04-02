from aiokafka import AIOKafkaConsumer
from src import settings


async def consume_handler():
    """Consume handler"""
    consumer = AIOKafkaConsumer(
        settings.KAFKA_TOPIC_DOWNLOAD,
        loop=settings.loop, bootstrap_servers=settings.BOOTSTRAP_SERVERS)

    await consumer.start()
    try:
        # Consume messages
        async for msg in consumer:
            if msg.topic == settings.KAFKA_TOPIC_DOWNLOAD:
                print(msg.value)
    finally:
        # Will leave consumer group; perform autocommit if enabled.
        await consumer.stop()
