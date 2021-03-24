from fastapi import FastAPI
from pydantic import BaseModel

from worker.celery_app import celery_app

import celery
from celery import result

# Create the FastAPI app
app = FastAPI()

# Use pydantic to keep track of the input request payload
class Numbers(BaseModel):
  x: float
  y: float

# REST endpoint to add a task to the job queue
@app.post('/add', status_code=202)
async def add(n: Numbers):
  task_name = 'worker.celery_worker.add'
  task = celery_app.send_task(task_name, args=[n.x, n.y])
  return { 'task_id': task.id }

# REST enpoint to get job status given the job id
@app.get('/status/{task_id}')
async def status(task_id: str) -> dict:
  res = result.AsyncResult(task_id)
  if res.state == celery.states.SUCCESS:
    return {'state': celery.states.SUCCESS, 'result': res.result}
  return {'state': res.state, }
