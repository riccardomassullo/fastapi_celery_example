# Requirements
pip install poetry

# Install dependencies
poetry install

# Upgrade dependencies
poetry update

# Enter in the virtualenv
poetry shell

# Run fastapi producer (REST endpoint)
uvicorn main:app --host 0.0.0.0 --port 8080

# Run Celery worker (with concurrency 4)
cd worker && celery worker --app=worker.celery_worker -c 4 --loglevel=info

# Run Flower service to monitor the queues
cd worker && flower -A celery_app

