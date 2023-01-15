#!/bin/bash
gunicorn --workers 2 --bind unix:/tmp/gunicorn.sock config.wsgi:application& 