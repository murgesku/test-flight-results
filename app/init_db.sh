#!/bin/sh

python manage.py migrate && \
python manage.py runscript init_db --traceback --dir-policy root