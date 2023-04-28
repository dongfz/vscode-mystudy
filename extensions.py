'''
Author: dfz
Date: 2023-04-26 19:59:52
LastEditTime: 2023-04-28 22:14:45
LastEditors: dfz
Description: 
FilePath: /mystudy/extensions.py
'''


import celery
import sqlalchemy
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_ECHO


_sqlalchemy_engine = sqlalchemy.create_engine(url=SQLALCHEMY_DATABASE_URI, echo=SQLALCHEMY_ECHO)



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
    
    




