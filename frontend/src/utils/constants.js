export const LISTING_STATUS = {
  DRAFT: 'draft',
  ACTIVE: 'active',
  INACTIVE: 'inactive',
  SOLD: 'sold',
};

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