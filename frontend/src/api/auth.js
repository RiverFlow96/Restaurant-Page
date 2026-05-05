import client from './client';

export const authApi = {
  login: (credentials) => client.post('/api/users/auth/login/', credentials),
  register: (data) => client.post('/api/users/auth/register/', data),
  logout: () => {
    localStorage.removeItem('token');
  },
  me: () => client.get('/api/users/auth/me/'),
};