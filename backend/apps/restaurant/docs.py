"""
Documentación de la API Restaurant v1

Base URL: /api/v1/restaurant/

---

## Endpoints públicos

### Menu (Menú)

**GET /menu/** - Listar platos del menú

Parámetros de query:
| Parámetro | Tipo | Descripción | Ejemplo |
|----------|------|-----------|---------|
| `page` | int | Página | `?page=1` |
| `page_size` | int | Items por página (max 100) | `?page_size=20` |
| `category` | str | Filtrar por categoría (slug) | `?category=entrantes` |
| `available` | bool | Filtrar por disponibilidad | `?available=true` |
| `search` | str | Buscar por nombre/descripción | `?search=risotto` |

**GET /menu/{id}/** - Ver plato específico

**POST /menu/** - Crear plato (admin)

**PUT /menu/{id}/** - Actualizar plato (admin)

**DELETE /menu/{id}/** - Eliminar plato (admin)

---

### Categories (Categorías)

**GET /categories/** - Listar categorías

Parámetros de query:
| Parámetro | Tipo | Descripción |
|----------|------|-----------|
| `search` | str | Buscar por nombre |
| `page` | int | Página |

**GET /categories/{id}/** - Ver categoría

---

### Reservations (Reservas)

**POST /reservations/** - Crear reserva

Campos requeridos:
```json
{
    "name": "string",
    "email": "email@ejemplo.com",
    "phone": "+34600000000",
    "date": "2026-06-01",
    "time": "20:00",
    "guests": 2
}
```

Campos opcionales:
- `special_requests`: "string"

Parámetros de query (admin):
| Parámetro | Descripción |
|----------|-----------|
| `status` | pending, confirmed, cancelled, completed |
| `date_from` | Fecha mínima (YYYY-MM-DD) |
| `date_to` | Fecha máxima (YYYY-MM-DD) |

---

### Gallery (Galería)

**GET /gallery/** - Listar imágenes

Parámetros de query:
| Parámetro | Tipo | Descripción |
|----------|------|-----------|
| `page` | int | Página |
| `page_size` | int | Items por página |

---

### Reviews (Reseñas)

**GET /reviews/** - Listar reseñas aprobadas

Parámetros de query:
| Parámetro | Descripción |
|----------|-----------|
| `rating` | Filtrar por puntuación (1-5) |

**POST /reviews/** - Crear reseña

Campos requeridos:
```json
{
    "client_name": "Nombre",
    "rating": 5,
    "comment": "Comentario"
}
```

---

### Contact (Contacto)

**GET /contact/** - Ver información de contacto

**POST /contact/** - Crear info de contacto (admin)

**PUT /contact/** - Actualizar info de contacto (admin)

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
| 500 | Error interno |

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