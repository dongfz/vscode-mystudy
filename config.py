'''
Author: dfz
Date: 2023-04-26 21:34:45
LastEditTime: 2023-04-28 22:29:44
LastEditors: dfz
Description: 
FilePath: /mystudy/config.py
'''

from celery.schedules import crontab


SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost/test?charset=utf8mb4'
SQLALCHEMY_ECHO = True


broker_url = 'redis://:123456@localhost:6379/1'
result_backend = 'redis://:123456@localhost:6379/2'
timezone = 'Asia/Shanghai'
enable_utc = True
imports = ('tasks',)

beat_schedule = {
    "test_sched_task": {
        "task": "tasks.test_sched_task",
        "schedule": crontab(minute="*/1"),
        "args": (1,)
    },
}
