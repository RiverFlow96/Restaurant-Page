.PHONY: help install dev build docker-up docker-down docker-build test lint pre-commit clean deploy-render deploy-cloudflare

help:
	@echo "Available commands:"
	@echo "  make install          - Install all dependencies"
	@echo "  make dev            - Run development servers"
	@echo "  make build         - Build for production"
	@echo "  make docker-up    - Start Docker containers"
	@echo "  make docker-down  - Stop Docker containers"
	@echo "  make docker-build - Build Docker images"
	@echo "  make test         - Run tests"
	@echo "  make lint         - Run linters"
	@echo "  make clean        - Clean temporary files"
	@echo "  make deploy-render     - Deploy to Render"
	@echo "  make deploy-cloudflare - Deploy to Cloudflare"

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

deploy-render:
	@echo "=== Deploy a Render ==="
	@echo ""
	@echo "1. Variables de entorno en Render Dashboard:"
	@echo "   - DEBUG=False"
	@echo "   - SECRET_KEY=your-secure-key"
	@echo "   - ALLOWED_HOSTS=your-app.onrender.com"
	@echo "   - DATABASE_URL=postgres://..."
	@echo ""
	@echo "2. O conecta tu repo en render.com y usa render.yaml"
	@echo ""
	@see "https://render.com/docs"

deploy-cloudflare:
	cd frontend && bun run build
	@echo "=== Deploy a Cloudflare Pages ==="
	@echo ""
	@echo "1. Variables en Cloudflare Dashboard:"
	@echo "   - VITE_API_URL=https://your-backend.onrender.com"
	@echo ""
	@echo "2. Despliega:"
	@echo "   wrangler pages project create"
	@echo "   wrangler pages deploy frontend/dist"
	@echo ""
	@echo "https://developers.cloudflare.com/pages"

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	rm -rf frontend/dist
	rm -rf .venv