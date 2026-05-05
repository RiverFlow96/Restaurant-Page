# Restaurant Web Page - Project Context

## Project Structure
- **Backend**: Django + Django REST Framework (in `/backend`)
- **Frontend**: Vue/React (in `/frontend`)
- **Database**: SQLite (db.sqlite3)

## Running the Backend

```bash
cd backend
uv run python manage.py runserver 0.0.0.0:8000
```

## Key Commands

```bash
# Apply migrations
uv run python manage.py migrate

# Create superuser (for admin panel)
uv run python manage.py createsuperuser
```

## Frontend Commands

```bash
cd frontend
bun install
bun run dev      # Development server
bun run build    # Production build
```

## API Endpoints (v1)

| Endpoint | Methods | Description |
|---------|---------|-------------|
| /api/v1/restaurant/menu/ | GET, POST | Menu items |
| /api/v1/restaurant/categories/ | GET, POST | Menu categories |
| /api/v1/restaurant/reservations/ | GET, POST | Restaurant reservations |
| /api/v1/restaurant/gallery/ | GET, POST | Gallery images |
| /api/v1/restaurant/reviews/ | GET, POST | Customer reviews |
| /api/v1/restaurant/contact/ | GET | Contact info |

## Frontend URLs
- Home: /
- API Docs: /api/docs/
- Admin: /admin/
- Browseable API: /api/v1/restaurant/menu/

## Template Locations
- Backend templates: /backend/templates/
- Custom home: api_home.html
- Custom docs: api_docs.html

## Key Files
- Settings: /backend/config/settings.py
- URLs: /backend/config/urls.py
- App: /backend/apps/restaurant/

## Important Notes
- Use `uv` for package management in backend (not pip)
- Use `bun` for package management in frontend (not npm)
- The .env file is required for DEBUG and ALLOWED_HOSTS
- Migrations must be applied after changes to models
- DRF browseable API is enabled (visit endpoints in browser)
