import { Routes, Route, Navigate } from 'react-router-dom';
import { useAuthStore } from '../store/authStore';

const ProtectedRoute = ({ children }) => {
  const isAuthenticated = useAuthStore((state) => state.isAuthenticated);
  return isAuthenticated ? children : <Navigate to="/login" />;
};

export const router = (
  <Routes>
    <Route path="/" element={<div>Home</div>} />
    <Route path="/listings" element={<div>Listings</div>} />
    <Route path="/listings/:id" element={<div>ListingDetail</div>} />
    <Route path="/login" element={<div>Login</div>} />
    <Route path="/register" element={<div>Register</div>} />
    <Route
      path="/create-listing"
      element={
        <ProtectedRoute>
          <div>CreateListing</div>
        </ProtectedRoute>
      }
    />
    <Route
      path="/my-listings"
      element={
        <ProtectedRoute>
          <div>MyListings</div>
        </ProtectedRoute>
      }
    />
    <Route path="/profile/:username" element={<div>UserProfile</div>} />
  </Routes>
);