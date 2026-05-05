.PHONY: help install dev build docker-up docker-down docker-build test lint pre-commit clean

help:
	@echo "Available commands:"
	@echo "  make install        - Install all dependencies"
	@echo "  make dev          - Run development servers"
	@echo "  make build       - Build for production"
	@echo "  make docker-up    - Start Docker containers"
	@echo "  make docker-down - Stop Docker containers"
	@echo "  make docker-build - Build Docker images"
	@echo "  make test       - Run tests"
	@echo "  make lint       - Run linters"
	@echo "  make clean     - Clean temporary files"

install:
	cd backend && uv pip install -r requirements.txt
	cd backend && uv pip install black isort
	cd frontend && bun install

dev:
	cd backend && uv run python manage.py runserver
	cd frontend && bun run dev

build:
	cd frontend && bun run build

docker-up:
	docker-compose up -d

docker-down:
	docker-compose down

docker-build:
	docker-compose build

test:
	@echo "No tests configured yet"

fmt:
	cd backend && black .
	cd backend && isort .

lint:
	cd backend && uv pip install black isort
	cd backend && black --check .
	cd backend && isort --check .

pre-commit:
	uv pip install pre-commit
	pre-commit install

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	rm -rf frontend/dist
	rm -rf .venv