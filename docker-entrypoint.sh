#!/bin/bash

echo "COLLECTING STATIC FILES..."
python manage.py collectstatic --noinput

echo "APPLYING DB MIGRATIONS..."
python manage.py migrate

echo "STARTING SERVER..."
python manage.py runserver 0.0.0.0:8000
