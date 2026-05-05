# Restaurant Web Page - Project Context

## Project Structure
- **Backend**: Django + Django REST Framework (`/backend`)
- **Frontend**: React + Vite + Tailwind (`/frontend`)
- **Database**: SQLite (db.sqlite3)

---

## Running the Project

### Backend
```bash
cd backend
pip install -r requirements.txt  # or: uv pip install -r requirements.txt
uv run python manage.py runserver 0.0.0.0:8000
```

### Frontend
```bash
cd frontend
bun run dev
bun run build
```

---

## Key Commands

### Backend
```bash
pip install -r requirements.txt  # Install dependencies
uv run python manage.py migrate         # Apply migrations
uv run python manage.py createsuperuser  # Create admin user
```

### Frontend
```bash
bun run dev      # Development server (localhost:5173)
bun run build    # Production build to /dist
bun run preview # Preview production build
```

---

## Architecture

### Backend API (Django REST Framework)
| Endpoint | Methods | Description |
|----------|---------|-------------|
| `/api/v1/restaurant/menu/` | GET, POST | Menu items |
| `/api/v1/restaurant/categories/` | GET, POST | Menu categories |
| `/api/v1/restaurant/reservations/` | GET, POST | Restaurant reservations |
| `/api/v1/restaurant/gallery/` | GET, POST | Gallery images |
| `/api/v1/restaurant/reviews/` | GET, POST | Customer reviews |
| `/api/v1/restaurant/contact/` | GET | Contact info |

### Frontend Structure
```
frontend/src/
├── App.jsx                 # Router setup
├── main.jsx                # Entry point
├── components/ui/         # Reusable UI components
│   ├── index.jsx         # Navbar, Footer, Button, Reveal, Section, Container
│   └── Icons.jsx         # Memoized SVG icons
├── pages/LandingPage/
│   ├── LandingPage.jsx  # Main page component
│   ├── sections.jsx     # Hero, About, MenuSection, Gallery, Contact
│   └── Reservation.jsx # Reservation form
├── router/index.jsx     # React Router config
├── store/appStore.js    # Zustand store (UI state)
└── utils/constants.js    # Restaurant data
```

---

## Frontend URLs
- Home: `/`
- API Docs: `/api/docs/`
- Admin: `/admin/`

---

## Key Files
- Backend settings: `/backend/config/settings.py`
- Backend URLs: `/backend/config/urls.py`
- Backend app: `/backend/apps/restaurant/`
- Frontend main: `/frontend/src/App.jsx`
- Frontend constants: `/frontend/src/utils/constants.js`

---

## Important Notes

### Package Managers
- **Backend**: `uv` (not pip)
- **Frontend**: `bun` (not npm)

### Environment
- `.env` file required for DEBUG and ALLOWED_HOSTS
- Migrations must be applied after model changes
- DRF browseable API enabled

### Frontend Best Practices (Applied)
- React.memo on all static components
- Memoized SVG Icons in separate file
- Constants hoisted outside components
- Zustand for state management
- Tailwind for styling

---

## Restaurant Info (Hardcoded)
- Name: Koniec - El Fin
- Type: Cuban restaurant
- Location: Barrio Los Rusos, Barbosa, La Lisa, La Habana, Cuba
- Hours: 9 AM - 10 PM daily
- Phone: 052500167