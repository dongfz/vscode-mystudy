'''
Author: dfz
Date: 2023-04-26 21:59:27
LastEditTime: 2023-06-15 20:35:15
LastEditors: dfz
Description: 
FilePath: /mystudy/mystudy/__init__.py
'''

from mystudy.extensions import BaseCeleryTask, CeleryApp


def create_celery_app() -> CeleryApp:
    celery_app = CeleryApp(__name__, task_cls=BaseCeleryTask)
    celery_app.config_from_object('mystudy.config')
    celery_app.set_default()
    return celery_app


celery_app = create_celery_app()
