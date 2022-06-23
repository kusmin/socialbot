sudo kill -9 $(lsof -t -i:9000)
cd docker
docker-compose up -d
cd ..

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic
gunicorn socialbot.wsgi:application --bind 0.0.0.0:9000

