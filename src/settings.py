from envparse import env

env.read_envfile()

# Debug
DEBUG = env('DEBUG', cast=bool, default=False)

# Application
APP_HOST = env('APP_HOST', cast=str, default='0.0.0.0')
APP_PORT = env('APP_PORT', cast=int, default=8080)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(process)d %(name)s %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG' if DEBUG else 'WARNING',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'aiohttp.access': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}