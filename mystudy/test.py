'''
Author: dfz
Date: 2023-04-24 22:36:45
LastEditTime: 2023-04-27 22:54:00
LastEditors: dfz
Description: 
FilePath: /mystudy/test.py
Software: vscode
'''

from . import celery_app

if __name__ == "__main__":
    celery_app.send_task('tasks.task1')


