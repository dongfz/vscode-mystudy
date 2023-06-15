'''
Author: dfz
Date: 2023-04-27 22:29:40
LastEditTime: 2023-05-07 21:38:46
LastEditors: dfz
Description: 
FilePath: /mystudy/main.py
Software: vscode
'''


from mystudy import celery_app

if __name__ == "__main__":
    celery_app.worker_main(argv=["worker"])
