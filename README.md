# Try Django

TODO: Add installation

Create `.env` file with your desire credentials
```
touch .env
echo "SECRET_KEY=2@@mnmn#=yeh_%0g!h-6bpbu4!j690@klk#srz2arhh7hmaq84" >> .env
echo "POSTGRESQL_USERNAME=admin" >> .env
echo "POSTGRESQL_PASSWORD=passwd" >> .env
echo "POSTGRESQL_DATABASE=pg" >> .env
```

Run
```bash
docker-compose up
```

Stop and remove volumes
```bash
docker-compose down --volumes
```

Bash into Postgres container
```bash
docker exec -it try-django-db-1 bash
```

Make migrations, migrate and load mock data
```bash
cd src
python manage.py makemigrations
```

```bash
python manage.py migrate --run-syncdb
```

```bash
python manage.py loaddata mock_data.json
```

```bash
python manage.py runserver 0.0.0.0:8000
```