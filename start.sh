cd docker
docker-compose up -d
cd ..

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
gunicorn socialbot.wsgi:application --bind 0.0.0.0:9000

