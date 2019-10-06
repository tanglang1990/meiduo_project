#!/bin/bash

cd /root/meiduo_project/meiduo_mall/
celery -A celery_tasks.main worker -l info