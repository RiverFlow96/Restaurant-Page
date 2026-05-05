import { useState, useEffect, useRef } from 'react'
import { Link } from 'react-router-dom'
import clsx from 'clsx'

export function Navbar() {
  const [scrolled, setScrolled] = useState(false)
  const [menuOpen, setMenuOpen] = useState(false)

  useEffect(() => {
    const handleScroll = () => setScrolled(window.scrollY > 50)
    window.addEventListener('scroll', handleScroll, { passive: true })
    return () => window.removeEventListener('scroll', handleScroll)
  }, [])

  const navLinks = [
    { to: '#menu', label: 'Menú' },
    { to: '#galeria', label: 'Galería' },
    { to: '#reservar', label: 'Reservar' },
  ]

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
          {navLinks.map((link) => (
            <Link key={link.to} to={link.to} className="text-white/80 hover:text-accent transition-colors">
              {link.label}
            </Link>
          ))}
        </div>
        
        <button className="md:hidden text-white p-2" onClick={() => setMenuOpen(!menuOpen)}>
          <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            {menuOpen 
              ? <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" /> 
              : <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
            }
          </svg>
        </button>
      </div>
      
      {menuOpen && (
        <div className="md:hidden bg-primary/95 backdrop-blur-md px-6 pb-4">
          {navLinks.map((link) => (
            <Link key={link.to} to={link.to} className="block py-2 text-white/80" onClick={() => setMenuOpen(false)}>
              {link.label}
            </Link>
          ))}
        </div>
      )}
    </nav>
  )
}

export function Footer() {
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
}

export function Button({ children, variant = 'primary', className, ...props }) {
  const variants = {
    primary: 'bg-accent text-primary hover:bg-accent-light',
    secondary: 'border-2 border-white text-white hover:bg-white/10',
    ghost: 'text-white/80 hover:text-accent',
  }
  
  return (
    <button className={clsx(
      'px-8 py-3 font-semibold rounded transition-colors',
      variants[variant],
      className
    )} {...props}>
      {children}
    </button>
  )
}

export function Reveal({ children, delay = 0 }) {
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
}

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