import { create } from 'zustand'

export const useAppStore = create((set) => ({
  menuTab: 'entrantes',
  reservationForm: {
    name: '',
    email: '',
    phone: '',
    guests: 2,
    date: '',
    time: '',
    message: '',
  },
  reservationSubmitted: false,
  galleryOpen: false,
  galleryIndex: 0,
  
  setMenuTab: (tab) => set({ menuTab: tab }),
  setReservationForm: (field, value) => set((state) => ({
    reservationForm: { ...state.reservationForm, [field]: value }
  })),
  resetReservationForm: () => set({
    reservationForm: {
      name: '',
      email: '',
      phone: '',
      guests: 2,
      date: '',
      time: '',
      message: '',
    },
    reservationSubmitted: false,
  }),
  submitReservation: () => set({ reservationSubmitted: true }),
  openGallery: (index) => set({ galleryOpen: true, galleryIndex: index }),
  closeGallery: () => set({ galleryOpen: false, galleryIndex: 0 }),
}))