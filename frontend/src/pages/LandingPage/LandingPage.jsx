import { Navbar, Footer } from '../../components/ui'
import { Hero, About, MenuSection, Gallery, Contact } from './sections'
import { Reservation } from './Reservation'

export function LandingPage() {
  return (
    <div className="min-h-screen bg-bg-dark">
      <Navbar />
      <Hero />
      <About />
      <MenuSection />
      <Gallery />
      <Reservation />
      <Contact />
      <Footer />
    </div>
  )
}