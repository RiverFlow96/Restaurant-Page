import { create } from 'zustand';
import { authApi } from '../api/auth';

export const useAuthStore = create((set, get) => ({
  user: null,
  token: localStorage.getItem('token'),
  isAuthenticated: !!localStorage.getItem('token'),
  isLoading: false,

  login: async (credentials) => {
    set({ isLoading: true });
    try {
      const response = await authApi.login(credentials);
      const { access, user } = response.data;
      localStorage.setItem('token', access);
      set({ user, token: access, isAuthenticated: true, isLoading: false });
      return true;
    } catch (error) {
      set({ isLoading: false });
      return false;
    }
  },

  register: async (data) => {
    set({ isLoading: true });
    try {
      const response = await authApi.register(data);
      const { access, user } = response.data;
      localStorage.setItem('token', access);
      set({ user, token: access, isAuthenticated: true, isLoading: false });
      return true;
    } catch (error) {
      set({ isLoading: false });
      return false;
    }
  },

  logout: () => {
    authApi.logout();
    set({ user: null, token: null, isAuthenticated: false });
  },

  fetchUser: async () => {
    if (!get().token) return;
    set({ isLoading: true });
    try {
      const response = await authApi.me();
      set({ user: response.data, isLoading: false });
    } catch (error) {
      get().logout();
    }
  },
}));