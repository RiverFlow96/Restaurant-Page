import { useState, useEffect, useRef, memo } from 'react'
import { Link } from 'react-router-dom'
import clsx from 'clsx'
import Icons from './Icons'

export const Navbar = memo(function Navbar() {
  const [scrolled, setScrolled] = useState(false)
  const [menuOpen, setMenuOpen] = useState(false)

  useEffect(() => {
    const handleScroll = () => setScrolled(window.scrollY > 50)
    window.addEventListener('scroll', handleScroll, { passive: true })
    return () => window.removeEventListener('scroll', handleScroll)
  }, [])

  const closeMenu = () => setMenuOpen(false)

  return (
    <nav className={clsx(
      'fixed top-0 left-0 right-0 z-50 transition-all duration-300',
      scrolled ? 'bg-primary/95 backdrop-blur-md shadow-lg' : 'bg-transparent'
    )}>
      <div className="max-w-6xl mx-auto px-6 py-4 flex items-center justify-between">
        <Link to="/" className="font-display text-2xl font-bold text-white">
          Koniec
        </Link>
        
        <div className="hidden md:flex items-center gap-8">
          {NAV_LINKS.map((link) => (
            <Link key={link.to} to={link.to} className="text-white/80 hover:text-accent transition-colors">
              {link.label}
            </Link>
          ))}
        </div>
        
        <button className="md:hidden text-white p-2" onClick={() => setMenuOpen(!menuOpen)} aria-label="Menu">
          {menuOpen ? <Icons.Close className="w-6 h-6" /> : <Icons.Menu className="w-6 h-6" />}
        </button>
      </div>
      
      {menuOpen && (
        <div className="md:hidden bg-primary/95 backdrop-blur-md px-6 pb-4">
          {NAV_LINKS.map((link) => (
            <Link key={link.to} to={link.to} className="block py-2 text-white/80" onClick={closeMenu}>
              {link.label}
            </Link>
          ))}
        </div>
      )}
    </nav>
  )
})

const NAV_LINKS = [
  { to: '#menu', label: 'Menú' },
  { to: '#galeria', label: 'Galería' },
  { to: '#reservar', label: 'Reservar' },
]

export const Footer = memo(function Footer() {
  const currentYear = new Date().getFullYear()
  
  return (
    <footer className="py-8 bg-primary border-t border-white/10">
      <div className="max-w-6xl mx-auto px-6 text-center">
        <p className="text-white/60">
          © {currentYear} Koniec - El Fin. Todos los derechos reservados.
        </p>
      </div>
    </footer>
  )
})

export const Button = memo(function Button({ children, variant = 'primary', className, ...props }) {
  return (
    <button className={clsx(
      'px-8 py-3 font-semibold rounded transition-colors',
      BUTTON_VARIANTS[variant],
      className
    )} {...props}>
      {children}
    </button>
  )
})

const BUTTON_VARIANTS = {
  primary: 'bg-accent text-primary hover:bg-accent-light',
  secondary: 'border-2 border-white text-white hover:bg-white/10',
  ghost: 'text-white/80 hover:text-accent',
}

export const Reveal = memo(function Reveal({ children, delay = 0 }) {
  const ref = useRef(null)
  const [visible, setVisible] = useState(false)

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([{ isIntersecting }]) => {
        if (isIntersecting) setVisible(true)
      },
      { threshold: 0.1 }
    )
    if (ref.current) observer.observe(ref.current)
    return () => observer.disconnect()
  }, [])

  return (
    <div 
      ref={ref} 
      className="transition-all duration-700"
      style={{ 
        opacity: visible ? 1 : 0, 
        transform: visible ? 'translateY(0)' : 'translateY(32px)',
        transitionDelay: `${delay}ms`
      }}
    >
      {children}
    </div>
  )
})

export function Section({ children, className, dark = false }) {
  return (
    <section className={clsx('py-20 md:py-32', dark ? 'bg-primary' : 'bg-bg', className)}>
      <div className="max-w-6xl mx-auto px-6">
        {children}
      </div>
    </section>
  )
}

export function Container({ children, className }) {
  return (
    <div className={clsx('max-w-6xl mx-auto px-6', className)}>
      {children}
    </div>
  )
}