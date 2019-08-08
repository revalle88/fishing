#!/bin/bash
wait-for-it -t 30 db
python manage.py makemigrations
until python manage.py migrate; do
  sleep 2
  echo "Retry!";
done
echo "Django is ready.";
exec "$@"