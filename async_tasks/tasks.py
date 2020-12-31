import json
import logging
import os

import requests
from celery import shared_task
from requests.models import HTTPError


@shared_task
def taskA():
    base_url = "http://music:8000/api/"
    resp = requests.get(base_url + "user/status")
    if resp.status_code != 200:
        email = os.environ.get("MUSIC_EMAIL")
        password = os.environ.get("MUSIC_PASSWORD")
        requests.get(base_url +
                     f"user/login?email={email}&password={password}")
    resp = requests.get(base_url + "user/status")
    if resp.status_code != 200:
        logging.error("failed to login")
        raise HTTPError
    resp = requests.get(base_url + "user/level")
    logging.info("current level:" + json.dumps(resp.json, indent=2))

    trigger_task_resp = requests.get(base_url + "tasks/task")

    resp = requests.get(base_url + "user/level")
    logging.info("current level:" + json.dumps(resp.json, indent=2))
