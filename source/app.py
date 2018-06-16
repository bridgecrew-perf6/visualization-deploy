# -*- coding: utf-8 -*-


from flask import Flask, request
from datetime import timedelta
import time
from celery import Celery
from celery_once import QueueOnce
from time import sleep


app = Flask(__name__)
app.config.from_object("config")

# # Initialize Celery
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])

celery.conf.ONCE = {
    'backend': 'celery_once.backends.Redis',
    'settings': {
        'url': app.config['CELERY_RESULT_BACKEND'],
        'default_timeout': 60 * 60
    }
}

celery.conf.CELERYBEAT_SCHEDULE = {
    'every-10-seconds': {
        'task': 'app.hello',
        'schedule': timedelta(seconds=10),
        'args': ('Hello World', )
    }
}


#同一时间只会有最多一个该任务在执行中，多余的任务请求将被丢弃
@celery.task(base=QueueOnce, once={'graceful': True})
def slow_task():
    sleep(30)
    now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    print('执行任务，现在时间：  ' + now)
    return "Done!"


#定时执行
@celery.task
def hello(message):
    print(message)
    #调用异步任务
    slow_task.apply_async()
    return message


@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        # 调用异步任务
        slow_task.apply_async()
        return "定时任务测试程序!"






