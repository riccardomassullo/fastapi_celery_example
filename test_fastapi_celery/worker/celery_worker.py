from celery import current_task
from .celery_app import celery_app

@celery_app.task()
def add(x: float, y: float) -> float:
    return x+y
