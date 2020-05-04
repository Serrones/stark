# VARIABLE ARGUMENTS
settings=settings.base

ifdef SETTINGS_FILE_FOR_DYNACONF
	settings=$(SETTINGS_FILE_FOR_DYNACONF)
else
	export SETTINGS_FILE_FOR_DYNACONF=$(settings)
endif

.PHONY: requirements run build up

clean: ## Clean local environment
	@find . -name "*__pycache__" -type d | xargs rm -rf
	@rm -f .coverage
	@rm -rf htmlcov/
	@rm -f coverage.xml
	@rm -f *.log

help:  ## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n\nTargets:\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

requirements: ## builds requirements.txt from poetry
	poetry export -f requirements.txt > requirements.txt

run: ## runs locally on port 8000
	poetry run uvicorn main:app --reload

build: ## builds docker images
	docker-compose build

up: ## spin development server in development mode at port 8009 using docker
	docker-compose up

test: clean ## Run tests
	echo $(SIMPLE_SETTINGS)
	poetry run pytest -x --rootdir=.

test-matching: clean ## Run matching tests
	poetry run pytest -x -k $(q) --pdb

test-debug: clean ## Run tests with pdb
	poetry run pytest -x --pdb

test-coverage: clean ## Run entire test suite with coverage
	poetry run pytest --cov=stark/backend/ --cov-report=html:htmlcov

