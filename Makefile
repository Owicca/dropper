all:
	/bin/false

PREFIX = dr

up:
	sudo docker compose up -d --build --force-recreate --remove-orphans
	sudo docker compose ps

start:
	sudo docker compose restart
	sudo docker compose ps

stop:
	sudo docker compose stop
	sudo docker compose ps

stats:
	sudo docker ps -q --filter "name=$(PREFIX)_*" | xargs sudo docker stats

ps:
	sudo docker compose ps

web:
	sudo docker exec -ti $(PREFIX)_web bash

db:
	sudo docker exec -it $(PREFIX)_db bash

adm:
	sudo docker exec -it $(PREFIX)_adm sh
