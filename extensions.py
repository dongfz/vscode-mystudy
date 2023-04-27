'''
Author: dfz
Date: 2023-04-26 19:59:52
LastEditTime: 2023-04-27 22:36:08
LastEditors: dfz
Description: 
FilePath: /mystudy/extensions.py
'''


import celery
import sqlalchemy
from celeryconfig import sqlalchemy_url, sqlalchemy_echo


_sqlalchemy_engine = sqlalchemy.create_engine(url=sqlalchemy_url, echo=sqlalchemy_echo)



class BaseCeleryTask(celery.Task):
    _engine = None

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print('{0!r} failed: {1!r}'.format(task_id, exc))

    @property
    def engine(self):
        if self._engine is None:
            return _sqlalchemy_engine
        return self._engine



class CeleryApp(celery.Celery):

    def gen_task_name(self, name, module):
        return super().gen_task_name(name, module)
    
    




