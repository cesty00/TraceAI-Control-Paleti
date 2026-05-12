import { useState } from 'react'
import MovementForm from '../components/MovementForm.jsx'
import MovementTable from '../components/MovementTable.jsx'

const initialMovements = [
  { id: 'PAL-MOV-0001', movement_type: 'RECEPTION', pallet_code: 'PAL-EUR-1200x800', quantity: 64, status: 'SYNCED' },
  { id: 'PAL-MOV-0002', movement_type: 'PRODUCTION_ALLOCATION', pallet_code: 'PAL-EUR-1200x800', quantity: 28, status: 'VALIDATED' },
]

export default function PalletMovements() {
  const [movements, setMovements] = useState(initialMovements)

  function addMovement(payload) {
    const movement = {
      id: `PAL-MOV-${String(movements.length + 1).padStart(4, '0')}`,
      movement_type: payload.movement_type,
      pallet_code: payload.pallet_code,
      quantity: payload.quantity,
      status: payload.quantity > 0 && payload.pallet_code ? 'VALIDATED' : 'ERROR',
    }
    setMovements((current) => [movement, ...current])
  }

  return (
    <section>
      <h2>Miscari paleti</h2>
      <MovementForm onSubmit={addMovement} />
      <MovementTable movements={movements} />
    </section>
  )
}
