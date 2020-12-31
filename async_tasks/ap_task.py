#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-12-31 15:43:32
# @Author  : Your Name (you@example.org)
# @Link    : link
# @Version : 1.0.0

import os

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor

from requests.models import HTTPError
import requests
import os
import logging
import json

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def task():
    base_url = "http://neserver/api/"
    resp = requests.get(base_url + "user/status")
    if resp.status_code != 200:
        email = os.environ.get("MUSIC_EMAIL")
        password = os.environ.get("MUSIC_PASSWORD")
        requests.get(base_url + f"user/login?email={email}&password={password}")
    resp = requests.get(base_url + "user/status")
    if resp.status_code != 200:
        logging.error("failed to login")
        raise HTTPError
    requests.get(base_url + "user/signin")
    resp = requests.get(base_url + "user/level")
    logging.info("current level:" + json.dumps(json.loads(resp.text), indent=2))

    trigger_task_resp = requests.get(base_url + "tasks/task")
    logging.info(
        "current level:" + json.dumps(json.loads(trigger_task_resp.text), indent=2)
    )
    resp = requests.get(base_url + "user/level")
    logging.info("after task level:" + json.dumps(json.loads(resp.text), indent=2))


if __name__ == "__main__":
    executors = {
        "default": ThreadPoolExecutor(10),
        "processpool": ProcessPoolExecutor(2),
    }
    job_defaults = {"coalesce": False, "max_instances": 2}
    sched = BlockingScheduler()
    sched.add_job(task, "cron", hour="10,15,22", jitter=120, **job_defaults)
    sched.start()
    # pass
    # task()
