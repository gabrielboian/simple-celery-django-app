from datetime import timedelta

from simple_celery_app.celery import app


@app.task(bind=True)
def new_task(self):
    sum = 1 + 2
    return sum

@app.task(bind=True)
def another_task(self):
    sum = 2 + 2
    return sum

@app.task(bind=True)
def all_tasks(self):
    new_task()
    another_task()
    return 'Its work'

# this approach run the task every time when the celery worker start
new_task.delay()