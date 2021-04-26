# A simple background tasks worker with Django + Celery

This is a simple app who helps you to create tasks running in background of your app.

You can use this simple app as a serverless or with your main app if you programming in python and use Django.

## Goals

The main goal of this sharing is helping other people when they need to deal with background tasks in a simple way.

## Requirements

You have to understand and have a knowledge with Python Language and a previous contact with Django.
Will be easier if you know a little of Docker.

For you testing this app you will need an instance of RabbitMQ and an instance of MySQL.

## Installation

It is very advisable that you use a [virtualenv](https://pypi.org/project/virtualenv/) to install the requirements of that application
```bash
pip install virtualenv

mkdir your-project-name

cd your-project-name

virtualenv -p python3 env

source env/bin/activate
```
After you do the previous step and clone the repo, get in where is the requirements.txt

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install this application.

```bash
pip install -r requirements.txt
```

## Useful

Using a Docker container is the easiest way to use this app.

With Docker:

```bash
docker run --name your_db_name -e MYSQL_ROOT_PASSWORD=YOUR_PASSWORD_HERE -p 3306:3306 -d mysql:5.7.34

docker run -d --hostname django-rabbit --name rabbit -p 8080:15672 rabbitmq:3-management
```

Here we install and run a container with MySQL, open 3306 port to allow external access.

After that we install RabbitMQ and open 8080 port to allow an http access to a dashboard who comes with the image.


## Usage

First of all go to the Settings.py inside of our app simple_celery_app and change this paths:

```python
CELERY_BROKER_URL='amqp://YOUR_USER:YOUR_PASSWORD@localhost' # RabbitMQ
CELERY_RESULT_BACKEND='db+mysql://YOUR_USER:YOUR_PASSWORD@localhost' #MYSQL
```

What we do here is save our results into MySQL and use RabbitMQ as a queue management.

Then go celery.py into simple_celery_app.

You will see some basics configurations of celery, this things I get from celery documentation.

Now we have some approach's.

Using the beat schedule as app.conf.beat_schedule, we have some configs to call our tasks inside of simple_task.tasks after a time we choose.

```python
from datetime import timedelta

app.conf.beat_schedule = {
    'run-every-ten-seconds': {
        'task': 'simple_task.tasks.new_task',
        'schedule': timedelta(seconds=10), # WE SET 10 SECONDS TO RUN THE TASK NAMED AS "NEW_TASK" INSIDE OF SIMPLE_TASK.TASKS
    },
    'run-all-tasks-at-the-same-time':{
        'task': 'simple_task.tasks.all_tasks', # THIS APPROACH LET US TO CALL ALL OF OUR TASKS IN ONE TASKS AND RUN THEY SIMULTANEITY
        'schedule': timedelta(seconds=15),
    },
}
```

To run this tasks we have to open 2 terminals and type the following commands.

```python
celery -A simple_celery_app worker --loglevel=INFO #This commands run the worker it self

celery -A simple_celery_app beat -l info #This command will run the schedule
```

If you don't want to schedule tasks you have to comment the app.conf.beat_schedule above and simple run:
```python

celery -A simple_celery_app worker --loglevel=INFO

```

You will see that the only new_task will run. This is because we call here inside de tasks.py when we put
```python
new_task.delay()
```
We use delay because it's an asynchronous task.


## Summary
This is a simple explanation of how celery works and I hope this helps you to get started with this powerful tool.

If you have any questions or any contribution to make please make your self comfortable to make pull request or reach me at github.

## License
[MIT](https://choosealicense.com/licenses/mit/)