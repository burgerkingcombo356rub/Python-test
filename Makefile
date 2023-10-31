build:
	docker compose build
run:
	docker compose build && docker compose up -d
restart:
	docker compose restart
stop:
	docker compose stop
migrations:
	docker exec -i backend bash -c 'alembic upgrade head'