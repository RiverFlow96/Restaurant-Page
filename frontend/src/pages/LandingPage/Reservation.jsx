import { useState } from 'react'
import { Reveal, Section, Container } from '../../components/ui'
import { Button } from '../../components/ui'
import { RESTAURANT } from '../../utils/constants'
import { useAppStore } from '../../store/appStore'

export function Reservation() {
  const { reservationForm, setReservationForm, reservationSubmitted, submitReservation, resetReservation } = useAppStore()
  
  const handleSubmit = (e) => {
    e.preventDefault()
    submitReservation()
  }

  if (reservationSubmitted) {
    return (
      <Section id="reservar" dark>
        <Container>
          <div className="max-w-xl mx-auto text-center">
            <div className="w-16 h-16 bg-accent rounded-full flex items-center justify-center mx-auto mb-6">
              <svg className="w-8 h-8 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
              </svg>
            </div>
            <h3 className="font-display text-3xl font-bold text-white mb-4">¡Reserva Enviada!</h3>
            <p className="text-white/60 mb-6">Gracias por tu reserva. Te contactaremos en breve para confirmar.</p>
            <button onClick={resetReservation} className="text-accent hover:underline">Hacer otra reserva</button>
          </div>
        </Container>
      </Section>
    )
  }

  return (
    <Section id="reservar" dark>
      <Container>
        <Reveal>
          <div className="text-center mb-12">
            <div className="w-16 h-1 bg-accent mx-auto mb-4" />
            <h2 className="font-display text-4xl md:text-5xl font-bold text-white mb-4">Reservar Mesa</h2>
            <p className="text-white/60">¡Te esperamos!</p>
          </div>
        </Reveal>
        
        <Reveal delay={150}>
          <form onSubmit={handleSubmit} className="max-w-2xl mx-auto space-y-4">
            <div className="grid md:grid-cols-2 gap-4">
              <input
                type="text"
                placeholder="Nombre"
                required
                value={reservationForm.name}
                onChange={(e) => setReservationForm('name', e.target.value)}
                className="w-full px-4 py-3 bg-white/10 border border-white/20 rounded text-white placeholder-white/40 focus:border-accent focus:outline-none"
              />
              <input
                type="email"
                placeholder="Email"
                required
                value={reservationForm.email}
                onChange={(e) => setReservationForm('email', e.target.value)}
                className="w-full px-4 py-3 bg-white/10 border border-white/20 rounded text-white placeholder-white/40 focus:border-accent focus:outline-none"
              />
            </div>
            <div className="grid md:grid-cols-3 gap-4">
              <input
                type="tel"
                placeholder="Teléfono"
                required
                value={reservationForm.phone}
                onChange={(e) => setReservationForm('phone', e.target.value)}
                className="w-full px-4 py-3 bg-white/10 border border-white/20 rounded text-white placeholder-white/40 focus:border-accent focus:outline-none"
              />
              <select
                value={reservationForm.guests}
                onChange={(e) => setReservationForm('guests', Number(e.target.value))}
                className="w-full px-4 py-3 bg-white/10 border border-white/20 rounded text-white focus:border-accent focus:outline-none"
              >
                {[2, 3, 4, 5, 6, 7, 8].map((n) => (
                  <option key={n} value={n} className="text-primary">{n} comensales</option>
                ))}
              </select>
              <input
                type="date"
                required
                value={reservationForm.date}
                onChange={(e) => setReservationForm('date', e.target.value)}
                className="w-full px-4 py-3 bg-white/10 border border-white/20 rounded text-white placeholder-white/40 focus:border-accent focus:outline-none"
              />
            </div>
            <textarea
              placeholder="Mensaje especial (alergías, ocasión, etc.)"
              rows={3}
              value={reservationForm.message}
              onChange={(e) => setReservationForm('message', e.target.value)}
              className="w-full px-4 py-3 bg-white/10 border border-white/20 rounded text-white placeholder-white/40 focus:border-accent focus:outline-none resize-none"
            />
            <Button variant="primary" type="submit" className="w-full">
              Enviar Reserva
            </Button>
          </form>
        </Reveal>
      </Container>
    </Section>
  )
}