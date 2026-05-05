import client from './client';

export const listingsApi = {
  getAll: (params) => client.get('/api/listings/', { params }),
  getById: (id) => client.get(`/api/listings/${id}/`),
  create: (data) => client.post('/api/listings/', data),
  update: (id, data) => client.patch(`/api/listings/${id}/`, data),
  delete: (id) => client.delete(`/api/listings/${id}/`),
};