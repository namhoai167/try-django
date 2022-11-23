# Try Django

TODO: Add installation

Build
```bash
docker-compose build
```

Run
```bash
docker-compose up
```

OR build and run
```bash
docker-compose up --build
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
docker-compose exec web python src/manage.py makemigrations
```

```bash
docker-compose exec web python src/manage.py migrate --run-syncdb
```

```bash
docker-compose exec web python src/manage.py loaddata src/mock_data.json
```

