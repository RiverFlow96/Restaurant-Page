import { Routes, Route } from 'react-router-dom'
import { LandingPage } from '../pages/LandingPage/LandingPage'

export const router = (
  <Routes>
    <Route path="/" element={<LandingPage />} />
  </Routes>
)