'''
Author: dfz
Date: 2023-04-26 21:34:45
LastEditTime: 2023-04-27 22:52:52
LastEditors: dfz
Description: 
FilePath: /mystudy/celeryconfig.py
'''
sqlalchemy_url = 'mysql+pymysql://root:123456@localhost/test?charset=utf8mb4'
sqlalchemy_echo = True
broker_url = 'redis://:123456@localhost:6379/1'
result_backend = 'redis://:123456@localhost:6379/2'
timezone = 'Asia/Shanghai'
enable_utc = True

imports = ('tasks',)
