'''
Author: dfz
Date: 2023-04-26 19:59:52
LastEditTime: 2023-06-15 23:26:13
LastEditors: dfz sneakydog@yeah.net
Description: 
FilePath: /mystudy/mystudy/extensions.py
'''


from celery import Celery, Task
import sqlalchemy
from mystudy.config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_ECHO


_engine = sqlalchemy.create_engine(
    url=SQLALCHEMY_DATABASE_URI, echo=SQLALCHEMY_ECHO)


class BaseCeleryTask(Task):
    _db = None

    def __call__(self, *args, **kwargs):
        print("TASK STARTING: {0.name}[{0.request.id}]".format(self))
        return self.run(*args, **kwargs)

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print('{0!r} failed: {1!r}'.format(task_id, exc))

    @property
    def db(self):
        if self._db is None:
            self._db = _engine
        return self._db


class CeleryApp(Celery):
    def gen_task_name(self, name, module):
        # if module.endswith(".tasks"):
        #     module = module[:-6]
        return super().gen_task_name(name, module)
