# TODO DETALLADO: Landing Page Restaurante (para Agente IA)

## SPEC DEL PROYECTO

**Tipo:** Landing page single-page con scroll animations
**Estilo:** Premium, inmersivo, profesional
**Target:** Clientes que buscan experiencia gastronómica

---

## RECURSOS PROPORCIONADOS

### Imágenes necesarias (solicitar al usuario):
- `hero-bg.mp4` o `hero-bg.jpg` — Video/foto para hero (1920x1080 min)
- `plate-1.jpg` — Foto de plato signature
- `plate-2.jpg` — Foto de entrée
- `plate-3.jpg` — Foto de dessert
- `restaurantInterior-1.jpg` — Foto interior
- `restaurantInterior-2.jpg` — Foto barra/zona
- `chef.jpg` — Foto del chef

### Copy a usar (proximamente):
- Nombre: [NOMBRE RESTAURANTE]
- Tagline: [TAGLINE]
- Dirección: [DIRECCIÓN]
- Teléfono: [TELÉFONO]
- Horario: [HORARIO]

---

## ESTRUCTURA DEL HTML

```
index.html
├── <style> (inline)
└── <body>
    ├── nav.navbar (fixed)
    ├── section.hero (fullscreen, video bg)
    │   ├── .hero-content
    │   │   ├── h1.title
    │   │   ├── p.tagline
    │   │   ├── a.cta-button
    │   │   └── .scroll-indicator
    ├── section.about
    │   ├── .about-text
    │   │   ├── h2
    │   │   └── p (Descripción)
    │   └── .chef-card
    │       ├── img.chef-photo
    │       └── .chef-info
    ├── section.menu (categorías tabs)
    │   ├── .menu-tabs
    │   │   └── button.tab (x3: Entrantes, Platos, Postres)
    │   └── .menu-grid
    │       └── .menu-card (x6-9 items)
    │           ├── img.plate
    │           ├── .menu-item-info
    │           │   ├── h4.name
    │           │   ├── p.description
    │           │   └── span.price
    ├── section.gallery (masonry/grid)
    │   └── .gallery-grid (x4-6 fotos)
    ├── section.reservation
    │   ├── .reservation-form
    │   │   ├── input.name
    │   │   ├── input.email
    │   │   ├── input.phone
    │   │   ├── select.guests (2-8)
    │   │   ├── input.date
    │   │   ├── input.time
    │   │   ├── textarea.special-requests
    │   │   └── button.submit
    │   └── .contact-info
    │       ├── .address
    │       ├── .phone
    │       ├── .hours
    │       └── .map-embed
    └── footer
        ├── .social-links
        └── .copyright
```

---

## REQUISITOS TÉCNICOS

### CSS (variables a usar):
```css
:root {
  --color-primary: #1a1a1a;       /* Negro profundo */
  --color-accent: #c9a456;     /* Dorado/dorado oscuro */
  --color-accent-light: #e8d5a3;
  --color-bg: #fafafa;          /* OFF-white */
  --color-bg-dark: #0d0d0d;
  --color-text: #1a1a1a;
  --color-text-light: #666666;
  --font-display: 'Playfair Display', serif;
  --font-body: 'Inter', sans-serif;
  --transition-smooth: 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}
```

### Animaciones (Scroll-triggered):
1. **Hero:** fade-in + scale-down sutil en load
2. **About:** slide-up cuando entra en viewport
3. **Menu Cards:** stagger fade-in (delay: 0.1s entre cada)
4. **Gallery:** scale-up en hover
5. **Sections:** fade-in-up al hacer scroll

### JavaScript requerido:
```javascript
// Intersection Observer para animaciones
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, { threshold: 0.1 });

// Menu tabs functionality
function switchTab(category) { ... }

// Smooth scroll para CTAs
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) { ... });
});

// Reservation form validation
function validateForm() { ... }
```

---

## FASE 1: Setup + Navbar + Hero

### 1.1 Setup HTML base
- [ ] DOCTYPE html + lang="es"
- [ ] Meta tags: charset, viewport, description, og:image
- [ ] Title: "[Nombre] | [Tagline]"
- [ ] Links: Google Fonts (Playfair Display, Inter)
- [ ] CSS Reset + variables

### 1.2 Navbar (fixed, transparent → solid on scroll)
- [ ] Logo (texto o imagen)
- [ ] Links: Menú, Galería, Reservar
- [ ] Estado: transparent al inicio, solid #0d0d0d después de 100px scroll
- [ ] Mobile: hamburger menu

### 1.3 Hero Section
- [ ] Video background (muted, autoplay, loop) O fallback image
- [ ] Overlay: rgba(0,0,0,0.4) para legibilidad
- [ ] Contenido centrado: h1 (font-display, 64px), p (24px), CTA button
- [ ] CTA Button: style primario con hover animation
- [ ] Scroll indicator: animation bounce-bottom

---

## FASE 2: About + Chef

### 2.1 About Section
- [ ] Grid: texto a la izq, imagen a la der (o al revés)
- [ ] h2 con línea decorativa (--color-accent)
- [ ] Párrafo de descripción (150-200 palabras)
- [ ] Botón "Ver Menú" secondary style

### 2.2 Chef Card (opcional, si hay foto)
- [ ] Imagen circular o rounded
- [ ] Nombre del chef
- [ ] Título/rol
- [ ] Quote corto

---

## FASE 3: Menú

### 3.1 Menu Section
- [ ] Tabs: Entrantes | Platos | Postres
- [ ] Grid de 3 columnas (desktop), 2 (tablet), 1 (mobile)
- [ ] Click tab → filtrar items con animation

### 3.2 Menu Card
- [ ] Imagen aspect-ratio 4:3
- [ ] Nombre del plato (h4, font-display)
- [ ] Descripción (p, color-text-light, max 2 líneas)
- [ ] Precio (span, --color-accent, bold)
- [ ] Hover: subtle scale + shadow

### 3.3 Sample Data (REEMPLAZAR con reales):
```javascript
const menuData = {
  entrantes: [
    { name: "Bruschetta de tomate", desc: "Pan artesano, tomates cherry, albahaca", price: "€12" },
    { name: "Carpaccio de ternera", desc: "Rúcula, parmesano, alcaparras", price: "€16" },
    { name: "Sopa del día", desc: "Variación según mercado", price: "€10" }
  ],
  platos: [
    { name: "Risotto de setas", desc: "Setas silvestres,.trufa, parmesano", price: "€24" },
    { name: "Pasta artesanal", desc: "Servicio de la casa", price: "€22" },
    { name: "Pescado del día", desc: "Según mercado", price: "€28" }
  ],
  postres: [
    { name: "Tiramisú", desc: "Receta tradicional", price: "€10" },
    { name: "Cheesecake", desc: "Frutos rojos", price: "€9" },
    { name: "Café especial", desc: " различных desserts", price: "€5" }
  ]
};
```

---

## FASE 4: Galería

### 4.1 Gallery Section
- [ ] Grid masonry o simple 2x3
- [ ] Imágenes: interior,食物, ambiente
- [ ] Hover: overlay con icono zoom + scale
- [ ] Lightbox al click (simple JS modal)

### 4.2 Imágenes:
- [ ] Usar placeholder de Unsplash si no hay fotos propias
- Keywords para buscar: restaurant interior, fine dining, plated food

---

## FASE 5: Reservas + Contacto

### 5.1 Reservation Section
- [ ] Form con validación
- [ ] Campos requeridos: nombre, email, teléfono, fecha, hora, comensales
- [ ] Submit → mostrar "Gracias, confirmaremos en X horas"
- [ ] Integración: OpenTable link O formspree O emailto

### 5.2 Contacto Info
- [ ] Dirección formateada
- [ ] Teléfono clickable (tel:)
- [ ] Email clickable (mailto:)
- [ ] Horario detallado
- [ ] Mapa (Google Maps embed o static image)

---

## FASE 6: Footer

### 6.1 Footer
- [ ] Logo
- [ ] Links rápidos
- [ ] Social icons: Instagram, Facebook, TripAdvisor
- [ ] Copyright + "Diseñado por [tu nombre]"

---

## FASE 7: Responsive

### Breakpoints:
```css
@media (max-width: 1024px) { ... } /* Laptop */
@media (max-width: 768px) { ... }  /* Tablet */
@media (max-width: 480px) { ... }  /* Mobile */
```

### Ajustes mobile:
- [ ] Navbar: hamburger menu
- [ ] Hero h1: 40px
- [ ] Sections padding: 60px vertical
- [ ] Menu grid: 1 columna
- [ ] Form: stacked fields

---

## FASE 8: Performance + SEO

### 8.1 SEO On-page
- [ ] Meta title: "Nombre | Tipo de comida | Ciudad"
- [ ] Meta description: 150-160 chars
- [ ] OG tags para social
- [ ] Schema.org Restaurant markup
- [ ] alt tags en todas las imágenes

### 8.2 Performance
- [ ] Lazy load imágenes (loading="lazy")
- [ ] Optimizar imágenes (WebP preferred)
- [ ] Minificar CSS/JS
- [ ] Google Fonts: display=swap

### 8.3 Analytics
- [ ] Google Analytics GA4
- [ ] Track: CTA clicks, form submissions
- [ ] Google Search Console verification

---

## ASSETS PENDIENTES DE USUARIO

- [ ] Fotos del restaurante (mínimo 6)
- [ ] Fotos del menú (mínimo 6)
- [ ] Foto del chef (opcional)
- [ ]copy: nombre, descripción, horarios
- [ ] Datos de contacto reales
- [ ] Sistema de reservas: OpenTable / propia / link externo

---

## CHECKLIST FINAL

- [ ] Validar HTML (W3C)
- [ ] Lighthouse performance > 90
- [ ] Lighthouse accessibility > 90
- [ ] Mobile responsive test
- [ ] Cross-browser test (Chrome, Safari, Firefox)
- [ ] Form submission test
- [ ] Smooth scroll test
- [ ] Animations disabled = still usable
- [ ] Imágenes cargan correctamente
- [ ] Mapa funciona