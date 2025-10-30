# project32-backend
project32-backend API


`docker compose down -v`


`docker compose up -d db`

`python3 manage.py makemigrations users`

`docker compose up --build -d web`

`docker compose exec web python manage.py makemigrations users`

`docker compose exec web python manage.py makemigrations`

`docker compose exec web python manage.py migrate`

`docker compose exec web python manage.py createsuperuser`

`docker compose exec web pytest --cov`

`docker compose exec web pytest -q`


CURL example:



curl -s -X POST http://localhost:8000/api/auth/logout/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <token>" \
  -d '{"refresh":"<token>"}'
