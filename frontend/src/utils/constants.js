<<<<<<< HEAD
export const RESTAURANT = {
  name: "Koniec - El Fin",
  shortName: "Koniec",
  tagline: "Sabor cubano, alma de острова",
=======
<<<<<<< Updated upstream
export const LISTING_STATUS = {
  DRAFT: 'draft',
  ACTIVE: 'active',
  INACTIVE: 'inactive',
  SOLD: 'sold',
};
=======
export const RESTAURANT = {
  name: "Koniec - El Fin",
  shortName: "Koniec",
  tagline: "Sabor cubano, alma de cuba",
>>>>>>> feature/devops
  phone: "052500167",
  email: "info@koniec.elfin",
  address: {
    street: "Barrio Los Rusos",
    city: "Barbosa, La Lisa",
    province: "La Habana",
    country: "Cuba",
    full: "Barrio Los Rusos, Barbosa, La Lisa, La Habana, Cuba",
    near: "Cerca de la Avenida 23",
  },
  hours: {
    daily: "9:00 AM a 10:00 PM",
    days: "Todos los días",
  },
  social: {
    instagram: "#",
    facebook: "#",
    tripadvisor: "#",
  },
  description: "Experimenta la auténtica gastronomía cubana en el corazón de La Habana. Nuestros platos tradicionales, preparados con recetas heredadas y los ingredientes más frescos, te transportarán a la isla de la manera más deliciosa.",
}
<<<<<<< HEAD
=======
>>>>>>> Stashed changes
>>>>>>> feature/devops

export const MENU = {
  entrantes: [
    { name: "Bruschetta Cubana", desc: "Pan tostado, frijoles negros, cerdo desmenuzado, plátano", price: "€8" },
    { name: "Carpaccio de Jamón", desc: "Jamón Serrano cubano, mango, lima, cilantro fresco", price: "€12" },
    { name: "Sopa de Malanga", desc: "Crema de malanga, coconut milk, ajo dorado", price: "€7" },
    { name: "Yuca con Mojo", desc: "Yuca hervida, salsa de ajo y cítricos", price: "€6" },
  ],
  platos: [
    { name: "Lechón Asado", desc: "Cerdo marinado 24h, naranjas, ají cubano, arroz moro", price: "€18" },
    { name: "Ropa Vieja", desc: "Carne deshecha, cebolla, pimientos, arroz congrí", price: "€16" },
    { name: "Arroz con Pollo", desc: "Pollo campesino, arroz amarillo, frijoles", price: "€15" },
    { name: "Paella Cubana", desc: "Mariscos, chorizo, maíz, azafrón criollo", price: "€22" },
    { name: "Moros y Cristianos", desc: "Frijoles negros y blancos, arroz, plátano", price: "€12" },
  ],
  postres: [
    { name: "Flan de Coconut", desc: "Flan de coco, caramelo dorado", price: "€7" },
    { name: "Pastel de Chocolate", desc: "Bizcocho de chocolate oscuro, frosting de café", price: "€8" },
    { name: "Arroz con Leche", desc: "Arroz dulce, vainilla, canela", price: "€6" },
    { name: "Tres Leches", desc: "Bizcocho mojado en tres leches, merengue", price: "€7" },
  ],
}

export const GALLERY_IMAGES = [
  "/Screenshot_20260505_113810.png",
  "/Screenshot_20260505_113814.png",
  "/Screenshot_20260505_113831.png",
  "/Screenshot_20260505_113803.png",
]

export const NAV_LINKS = [
  { to: "#menu", label: "Menú" },
  { to: "#galeria", label: "Galería" },
  { to: "#reservar", label: "Reservar" },
]

export const MENU_TABS = [
  { key: "entrantes", label: "Entrantes" },
  { key: "platos", label: "Platos Principales" },
  { key: "postres", label: "Postres" },
]