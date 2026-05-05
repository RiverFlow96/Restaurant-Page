"""
Documentación de la API Restaurant v1

Base URL: /api/v1/restaurant/

---

## NUEVO: Documentación Interactiva

Swagger UI: /api/docs/
Redoc: /api/redoc/

---

## Rate Limiting

| Endpoint | Límite |
|---------|--------|
| General (anon) | 100/hour |
| General (user) | 1000/hour |
| Reservations | 10/hour |
| Reviews | 5/hour |

---

## Sorting (ordenación)

Parámetro: `?ordering=field` o `?-field` (descendente)

| Endpoint | Campos disponibles |
|----------|---------------|
| `/menu/` | name, price, order, created_at |
| `/categories/` | name, order, created_at |
| `/reservations/` | date, time, created_at |
| `/gallery/` | order, created_at |
| `/reviews/` | rating, created_at |

Ejemplos:
- `?ordering=price` (menor a mayor)
- `?ordering=-price` (mayor a menor)
- `?ordering=-created_at` (más recientes)

---

## Filtering Avanzado

### Menu
| Parámetro | Descripción |
|----------|-----------|
| `category` | slug de categoría |
| `available` | true/false |
| `price_min` | precio mínimo (gte) |
| `price_max` | precio máximo (lte) |
| `search` | buscar en nombre/descripción |

### Reservations
| Parámetro | Descripción |
|----------|-----------|
| `status` | pending, confirmed, cancelled, completed |
| `date_from` | fecha mínima |
| `date_to` | fecha máxima |
| `guests` | número exacto |
| `guests_min` | mínimo de comensales |
| `guests_max` | máximo de comensales |

### Reviews
| Parámetro | Descripción |
|----------|-----------|
| `rating` | puntuación exacta |
| `rating_min` | puntuación mínima |
| `rating_max` | puntuación máxima |

---

## Endpoints

### Menu

**GET /menu/** - Listar platos
**GET /menu/{id}/** - Ver plato
**POST /menu/** - Crear (admin)
**PUT /menu/{id}/** - Actualizar (admin)
**DELETE /menu/{id}/** - Eliminar (admin)

### Categories

**GET /categories/** - Listar categorías
**GET /categories/{id}/** - Ver categoría
**POST /categories/** - Crear (admin)

### Reservations

**POST /reservations/** - Crear reserva

### Gallery

**GET /gallery/** - Listar imágenes

### Reviews

**GET /reviews/** - Listar reseñas
**POST /reviews/** - Crear reseña

### Contact

**GET /contact/** - Ver contacto

---

## Códigos de estado

| Código | Significado |
|--------|-------------|
| 200 | OK |
| 201 | Creado |
| 400 | Bad Request |
| 401 | No autorizado |
| 403 | Prohibido |
| 404 | No encontrado |
| 422 | Error de validación |
| 429 | Rate limit excedido |
| 500 | Error interno |

---

## Formato de respuesta paginada

```json
{
    "count": 50,
    "next": "http://localhost:8000/api/v1/restaurant/menu/?page=2",
    "previous": null,
    "results": [...]
}
```

## Formato de error

```json
{
    "error": "ValidationError",
    "message": "Datos inválidos",
    "timestamp": "2026-05-05T12:00:00",
    "details": {"campo": ["mensaje"]}
}
```
"""