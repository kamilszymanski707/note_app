#!/bin/bash

echo "APPLYING DB MIGRATIONS..."
python manage.py migrate

echo "STARTING SERVER..."
python manage.py runserver 0.0.0.0:8000
