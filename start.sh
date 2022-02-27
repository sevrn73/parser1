#!/bin/bash
source /home/sevrn/Documents/GitHub/env/bin/activate
exec gunicorn  -c "/home/sevrn/Documents/GitHub/parser1-main/gunicorn_config.py" parser1.wsgi 