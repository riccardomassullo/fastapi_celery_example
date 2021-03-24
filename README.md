## Requirements
Poetry is required to manage dependencies and Virtualenvs without creating a mess
```
pip install poetry
```

We also need redis as a message broker, so install redis. (Also RabbitMQ is supported)

## Install dependencies
Install dependencies declared in pyproject.toml file
```
poetry install
```

## Upgrade dependencies
If dependencies are added/deleted to pyproject.toml, use poetry to update them
```
poetry update
```

## Enter in the virtualenv
```
poetry shell
```

## Run fastapi producer (REST endpoint)
```
uvicorn main:app --host 0.0.0.0 --port 8080
```
OpenAPI panel with API documentation is at http://localhost:8080/docs

## Run Celery worker (with concurrency 4)
```
cd worker && celery worker --app=worker.celery_worker -c 4 --loglevel=info
```

## Run Flower service to monitor the queues
```
cd worker && flower -A celery_app
```
Flower panel is at http://localhost:5555
