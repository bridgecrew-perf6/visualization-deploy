# -*- coding: utf-8 -*-

WEB_PORT = 9090

SECRET_KEY = 'top-secret!'

# Celery configuration

#rabbitmq
CELERY_BROKER_URL = 'amqp://guest:guest@localhost//'
#redis
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'


