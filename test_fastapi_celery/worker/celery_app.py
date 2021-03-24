from celery import Celery

celery_app = Celery(
    "worker",
    backend = "redis://localhost/",
    broker = "redis://localhost/"
)

celery_app.conf.update(task_track_started=True)
