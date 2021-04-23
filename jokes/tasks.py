from __future__ import absolute_import, unicode_literals
import random
from celery.decorators import task
import requests
import time


@task(name="get_the_joke1")
def get_joke1():
    url = 'http://api.icndb.com/jokes/random/'
    response = requests.get(url).json()
    joke = response['value']['joke']
    return joke

@task(name="get_the_joke2")
def get_joke2():
    time.sleep(4)
    ab = "Message from another"
    return ab
