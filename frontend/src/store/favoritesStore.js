import { create } from 'zustand';
import { persist } from 'zustand/middleware';

export const useFavoritesStore = create(
  persist(
    (set, get) => ({
      favorites: [],

      addFavorite: (listingId) => {
        const { favorites } = get();
        if (!favorites.includes(listingId)) {
          set({ favorites: [...favorites, listingId] });
        }
      },

      removeFavorite: (listingId) => {
        const { favorites } = get();
        set({ favorites: favorites.filter((id) => id !== listingId) });
      },

      isFavorite: (listingId) => {
        return get().favorites.includes(listingId);
      },

      toggleFavorite: (listingId) => {
        const { favorites } = get();
        if (favorites.includes(listingId)) {
          set({ favorites: favorites.filter((id) => id !== listingId) });
        } else {
          set({ favorites: [...favorites, listingId] });
        }
      },
    }),
    {
      name: 'favorites-storage',
    }
  )
);