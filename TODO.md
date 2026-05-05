# TODO: Landing Page Restaurante

## ✅ COMPLETADO
- [x] Hero con imagen de fondo
- [x] Diseño responsive
- [x] Sección de menú con categorías (tabs)
- [x] Galería de imágenes
- [x].Formulario de reservas
- [x] Info de contacto
- [x] Paleta de colores configurada
- [x] Tipografía (Playfair Display + DM Sans)
- [x] Fotos del restaurante

---

## FRONTEND: Mejoras para Producción

### Estructura
- [ ] Dividir sections.jsx en archivos separados (Hero.jsx, About.jsx, MenuSection.jsx, Gallery.jsx, Contact.jsx)
- [ ] Crear componente Error Boundary
- [ ] Agregar Loading states a las secciones
- [ ] Instalar class-variance-authority para botones

### API Integration
- [ ] Crear API client en src/api/client.js
- [ ] Crear hook useMenu para traer datos del backend
- [ ] Crear hook useReservations para enviar reservas
- [ ] Conectar formulario con endpoint /api/v1/restaurant/reservations/

### SEO
- [ ] Agregar Meta tags dinámicos por página
- [ ] Agregar JSON-LD Schema Restaurant
- [ ] Agregar Open Graph tags

### Testing
- [ ] Configurar Vitest
- [ ] Crear tests básicos de componentes

---

## BACKEND: API (Completado ✅)
- [x] Paginación (page, page_size)
- [x] Versionado (/api/v1/)
- [x] Errores estandarizados
- [x] Filtros (?category=slug&available=true)
- [x] HATEOAS (_links)

---

## PENDIENTE FINAL
- [ ] Testing en dispositivos reales
- [ ] Analytics (Google Analytics o similar)
- [ ] Optimizar imágenes (WebP)
- [ ] Sistema de reservas definitivo (API + email o OpenTable)