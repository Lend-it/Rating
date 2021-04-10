SHELL := /bin/bash # Use bash syntax
CURRENT_DIR := $(shell pwd)
RUNNING_NETWORK := $(shell sudo docker network ls -f name=lendit_gateway | grep lendit_gateway )


build:
	chmod +x entrypoint.sh
	sudo docker-compose -f docker-compose.dev.yml build

run:
	@if [[ -n "${RUNNING_NETWORK}" ]]; then \
		sudo docker-compose -f docker-compose.dev.yml up; \
	else \
		sudo docker network create lendit_gateway; \
		sudo docker-compose -f docker-compose.dev.yml up; \
	fi
	

run-silent:
	@if [[ -n "${RUNNING_NETWORK}" ]]; then \
		sudo docker-compose -f docker-compose.dev.yml up -d; \
	else \
		sudo docker network create lendit_gateway; \
		sudo docker-compose -f docker-compose.dev.yml up -d; \
	fi

run-build:
	@if [[ -n "${RUNNING_NETWORK}" ]]; then \
		chmod +x entrypoint.sh; \
		sudo docker-compose -f docker-compose.dev.yml up --build; \
	else \
		chmod +x entrypoint.sh; \
		sudo docker network create lendit_gateway; \
		sudo docker-compose -f docker-compose.dev.yml up --build; \
	fi

test:
	sudo docker-compose -f docker-compose.dev.yml run rating python manage.py test

lint:
	sudo docker-compose -f docker-compose.dev.yml run rating black .

check-db:
	sudo docker-compose -f docker-compose.dev.yml exec db psql -U postgres

down:
	sudo docker-compose -f docker-compose.dev.yml down

recreate-db:
	sudo docker-compose -f docker-compose.dev.yml run rating python manage.py recreate-db

cov-html:
	sudo docker-compose -f docker-compose.dev.yml run rating python manage.py cov;
	google-chrome  $(CURRENT_DIR)/htmlcov/index.html;
