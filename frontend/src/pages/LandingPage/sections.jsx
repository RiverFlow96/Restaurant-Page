import { memo } from 'react'
import { Button, Reveal, Section, Container } from '../../components/ui'
import Icons from '../../components/ui/Icons'
import { RESTAURANT, MENU, GALLERY_IMAGES, MENU_TABS } from '../../utils/constants'
import { useAppStore } from '../../store/appStore'

export const Hero = memo(function Hero() {
  return (
    <section className="relative h-screen flex items-center justify-center overflow-hidden">
      <div className="absolute inset-0 bg-gradient-to-r from-primary via-primary/80 to-primary/40 z-10" />
      <div className="absolute inset-0 bg-[url('/Screenshot_20260505_113755.png')] bg-cover bg-center opacity-60" />
      
      <div className="relative z-20 text-center text-white px-6">
        <Reveal>
          <h1 className="font-display text-5xl md:text-7xl font-bold mb-4">
            {RESTAURANT.name}
          </h1>
        </Reveal>
        
        <Reveal delay={150}>
          <p className="text-xl md:text-2xl text-accent mb-8 font-body">{RESTAURANT.tagline}</p>
        </Reveal>
        
        <Reveal delay={300}>
          <p className="text-lg text-white/80 mb-8 max-w-xl mx-auto">{RESTAURANT.description}</p>
        </Reveal>
        
        <Reveal delay={450}>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <a href="#reservar">
              <Button variant="primary">Reservar Mesa</Button>
            </a>
            <a href="#menu">
              <Button variant="secondary">Ver Menú</Button>
            </a>
          </div>
        </Reveal>
      </div>
      
      <div className="absolute bottom-8 left-1/2 -translate-x-1/2 animate-bounce">
        <Icons.ChevronDown className="w-6 h-6 text-white/60" />
      </div>
    </section>
  )
})

export const About = memo(function About() {
  return (
    <Section>
      <Reveal>
        <div className="grid md:grid-cols-2 gap-12 items-center">
          <div className="space-y-6">
            <div className="w-16 h-1 bg-accent" />
            <h2 className="font-display text-4xl md:text-5xl font-bold text-primary">
              Sabores de<br />Cuba
            </h2>
            <p className="text-lg text-gray-600 leading-relaxed">
              {RESTAURANT.description}
            </p>
            <p className="text-lg text-gray-600 leading-relaxed">
              Cada plato cuenta una historia. Nuestras recetas han pasado de generación en generación, manteniendo la tradición y el amor por la buena comida.
            </p>
          </div>
          <div className="relative">
            <div className="aspect-[4/3] rounded-lg overflow-hidden shadow-2xl">
              <img src="/Screenshot_20260505_113803.png" alt="Ambiente del restaurante" className="w-full h-full object-cover" />
            </div>
            <div className="absolute -bottom-4 -right-4 w-32 h-32 bg-accent rounded-lg -z-10" />
          </div>
        </div>
      </Reveal>
    </Section>
  )
})

export const MenuSection = memo(function MenuSection() {
  const { menuTab, setMenuTab } = useAppStore()
  const menuItems = MENU[menuTab]
  const menuTabs = MENU_TABS
  
  return (
    <Section id="menu" dark>
      <Reveal>
        <div className="text-center mb-12">
          <div className="w-16 h-1 bg-accent mx-auto mb-4" />
          <h2 className="font-display text-4xl md:text-5xl font-bold text-white mb-4">Nuestra Carta</h2>
          <p className="text-white/60">Ingredientes frescos, recetas auténticas</p>
        </div>
      </Reveal>
      
      <Reveal delay={150}>
        <div className="flex justify-center gap-2 mb-12 flex-wrap">
          {menuTabs.map((tab) => (
            <button
              key={tab.key}
              onClick={() => setMenuTab(tab.key)}
              className={`px-6 py-2 rounded-full font-medium transition-all ${
                menuTab === tab.key
                  ? 'bg-accent text-primary'
                  : 'bg-white/10 text-white hover:bg-white/20'
              }`}
            >
              {tab.label}
            </button>
          ))}
        </div>
      </Reveal>
      
      <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
        {menuItems.map((item, index) => (
          <Reveal key={item.name} delay={index * 100}>
            <div className="bg-white/5 rounded-lg p-6 hover:bg-white/10 transition-colors group">
              <h3 className="font-display text-xl font-semibold text-white mb-2 group-hover:text-accent transition-colors">
                {item.name}
              </h3>
              <p className="text-white/60 text-sm mb-4">{item.desc}</p>
              <span className="text-accent font-semibold">{item.price}</span>
            </div>
          </Reveal>
        ))}
      </div>
    </Section>
  )
})

export const Gallery = memo(function Gallery() {
  return (
    <Section id="galeria">
      <Reveal>
        <div className="text-center mb-12">
          <div className="w-16 h-1 bg-accent mx-auto mb-4" />
          <h2 className="font-display text-4xl md:text-5xl font-bold text-primary mb-4">Galería</h2>
          <p className="text-gray-600">Nuestra cocina, nuestro ambiente</p>
        </div>
      </Reveal>
      
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
        {GALLERY_IMAGES.map((src, index) => (
          <Reveal key={index} delay={index * 100}>
            <div className="aspect-square rounded-lg overflow-hidden group">
              <img src={src} alt={`Galería ${index + 1}`} className="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500" />
            </div>
          </Reveal>
        ))}
      </div>
    </Section>
  )
})

export const Contact = memo(function Contact() {
  return (
    <section className="py-20 md:py-32 bg-bg-dark">
      <Container>
        <Reveal>
          <div className="text-center">
            <h2 className="font-display text-3xl md:text-4xl font-bold text-white mb-8">Contacto</h2>
            <div className="grid md:grid-cols-3 gap-8">
              <div className="space-y-2">
                <div className="w-12 h-12 bg-accent/20 rounded-full flex items-center justify-center mx-auto mb-4">
                  <Icons.MapPin className="w-6 h-6 text-accent" />
                </div>
                <p className="text-white font-medium">{RESTAURANT.address.full}</p>
                <p className="text-white/60 text-sm">{RESTAURANT.address.near}</p>
              </div>
              <div className="space-y-2">
                <div className="w-12 h-12 bg-accent/20 rounded-full flex items-center justify-center mx-auto mb-4">
                  <Icons.Phone className="w-6 h-6 text-accent" />
                </div>
                <a href={`tel:${RESTAURANT.phone}`} className="text-white hover:text-accent transition-colors">{RESTAURANT.phone}</a>
                <p className="text-white/60 text-sm">Teléfono</p>
              </div>
              <div className="space-y-2">
                <div className="w-12 h-12 bg-accent/20 rounded-full flex items-center justify-center mx-auto mb-4">
                  <Icons.Clock className="w-6 h-6 text-accent" />
                </div>
                <p className="text-white font-medium">{RESTAURANT.hours.daily}</p>
                <p className="text-white/60 text-sm">{RESTAURANT.hours.days}</p>
              </div>
            </div>
          </div>
        </Reveal>
      </Container>
    </section>
  )
})