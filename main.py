
"""
Author: dfz
Date: 2023-04-27 22:29:40
LastEditTime: 2023-06-15 23:12:32
LastEditors: dfz
Description: 
FilePath: /mystudy/main.py
Software: vscode
"""


from mystudy import celery_app

if __name__ == "__main__":
    celery_app.worker_main(
        argv=[
            "worker",
            "--beat",
            "--concurrency=4",
            "--loglevel=INFO",
            "--hostname=%h",
            "--pool=threads",
            # "--queues=test.q,test.2q",
            "--task-events",
        ]
    )
