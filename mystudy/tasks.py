
"""
Author: dfz
Date: 2023-04-26 19:59:21
LastEditTime: 2023-06-15 22:53:49
LastEditors: dfz
Description: 
FilePath: /mystudy/mystudy/tasks.py
"""

from celery import shared_task, current_app


@shared_task(bind=True)
def task1(self):
    print("tsat1")
    print(self)
    db = self.db
    with db.connect() as conn:
        print(conn)


@shared_task(bind=True)
def test_sched_task(self, test: int) -> None:
    print(test)
    print(current_app)
    current_app.send_task("mystudy.tasks.task1")
