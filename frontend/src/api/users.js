import client from './client';

export const usersApi = {
  getAll: () => client.get('/api/users/'),
  getByUsername: (username) => client.get(`/api/users/${username}/`),
  update: (username, data) => client.patch(`/api/users/${username}/`, data),
};