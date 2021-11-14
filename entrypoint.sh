#!/bin/bash

# Execute startup scripts
./wait-for-postgres.sh $DB_HOST
python manage.py collectstatic
python manage.py migrate
python manage.py runserver 0.0.0.0:8000