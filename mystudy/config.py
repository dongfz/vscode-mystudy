"""
Author: dfz
Date: 2023-04-26 21:34:45
LastEditTime: 2023-06-15 22:51:34
LastEditors: dfz
Description: 
FilePath: /mystudy/mystudy/config.py
Software: vscode
"""
from celery.schedules import crontab


SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@localhost/test?charset=utf8mb4"
SQLALCHEMY_ECHO = True


broker_connection_retry_on_startup = True
broker_url = "amqp://rabbit:123456@localhost/test"
result_backend = "rpc://"
timezone = "Asia/Shanghai"
enable_utc = True
imports = ("mystudy.tasks",)

beat_schedule = {
    "test_sched_task": {
        "task": "mystudy.test_sched_task",
        "schedule": crontab(minute="*/1"),
        "args": (1,),
    },
}
