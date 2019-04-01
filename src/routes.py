from src.apps.kafka.apps import kafka_app


def setup_routes(app):
    """Setup application routes"""
    app.add_subapp('/kafka/', kafka_app)
