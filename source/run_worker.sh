#!/bin/bash

celery -A app:celery worker -B --loglevel=INFO

