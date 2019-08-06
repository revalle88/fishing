#!/bin/bash
python manage.py makemigrations
until python manage.py migrate; do
  sleep 2
  echo "Retry!";
done
echo "Django is ready.";