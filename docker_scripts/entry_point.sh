python manage.py makemigrations app
until python manage.py migrate; do
  sleep 2
  echo "Retry!";
done
echo "Django is ready.";