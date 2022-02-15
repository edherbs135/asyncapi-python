.DEFAULT_GOAL := install

.PHONY: install
install:
	pip install .

.PHONY: install-test-deps
install-test-deps:
	pip install '.[test]'

.PHONY: sample-server
sample-server:
	uvicorn asyncapi.sample:app --reload

.PHONY: lint
lint: flake8 black mypy isort

.PHONY: flake8
flake8:
	pflake8

.PHONY: black
black:
	black .

.PHONY: mypy
mypy:
	mypy

.PHONY: isort
isort:
	isort .

.PHONY: test
test:
	pytest

