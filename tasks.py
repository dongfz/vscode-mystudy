'''
Author: dfz
Date: 2023-04-26 19:59:21
LastEditTime: 2023-04-27 22:57:48
LastEditors: dfz
Description: 
FilePath: /mystudy/tasks.py
'''

from celery import shared_task



@shared_task(bind = True)
def task1(self):
    print("tsat1")
    print(self)
    engine = self.engine
    with engine.connect() as conn:
        print(conn)