import { useState } from 'react'

export default function MovementForm({ onSubmit }) {
  const [form, setForm] = useState({
    movement_type: 'RECEPTION',
    pallet_code: 'PAL-EUR-1200x800',
    quantity: 1,
    source_location: '',
    target_location: 'WMS_PALETI_BUNI',
  })

  function update(field, value) {
    setForm((current) => ({ ...current, [field]: value }))
  }

  function submit(event) {
    event.preventDefault()
    onSubmit({ ...form, quantity: Number(form.quantity) })
  }

  return (
    <form className="form" onSubmit={submit}>
      <label>
        Tip miscare
        <select value={form.movement_type} onChange={(event) => update('movement_type', event.target.value)}>
          <option>RECEPTION</option>
          <option>INTERNAL_TRANSFER</option>
          <option>PRODUCTION_ALLOCATION</option>
          <option>DELIVERY</option>
          <option>CUSTOMER_RETURN</option>
        </select>
      </label>
      <label>
        Cod palet
        <input value={form.pallet_code} onChange={(event) => update('pallet_code', event.target.value)} />
      </label>
      <label>
        Cantitate
        <input type="number" min="1" value={form.quantity} onChange={(event) => update('quantity', event.target.value)} />
      </label>
      <label>
        Sursa
        <input value={form.source_location} onChange={(event) => update('source_location', event.target.value)} />
      </label>
      <label>
        Destinatie
        <input value={form.target_location} onChange={(event) => update('target_location', event.target.value)} />
      </label>
      <button type="submit">Adauga miscare demo</button>
    </form>
  )
}
