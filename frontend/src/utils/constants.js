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
>>>>>>> Stashed changes

export const LISTING_STATUS_LABELS = {
  [LISTING_STATUS.DRAFT]: 'Borrador',
  [LISTING_STATUS.ACTIVE]: 'Activo',
  [LISTING_STATUS.INACTIVE]: 'Inactivo',
  [LISTING_STATUS.SOLD]: 'Vendido',
};

export const REPORT_REASONS = [
  { value: 'spam', label: 'Spam' },
  { value: 'fraud', label: 'Fraude' },
  { value: 'inappropriate', label: 'Contenido inapropiado' },
  { value: 'prohibited', label: 'Producto prohibido' },
  { value: 'other', label: 'Otro' },
];