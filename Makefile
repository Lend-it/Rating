build:
	sudo docker-compose -f docker-compose.dev.yml build

run:
	sudo docker-compose -f docker-compose.dev.yml up

run-silent:
	sudo docker-compose -f docker-compose.dev.yml up -d

test:
	sudo docker-compose -f docker-compose.dev.yml run rating python manage.py test

run-build:
	sudo docker-compose -f docker-compose.dev.yml up --build

db:
	sudo docker-compose -f docker-compose.dev.yml exec db psql -U postgres

down:
	sudo docker-compose -f docker-compose.dev.yml down