const stock = [
  { pallet_code: 'PAL-EUR-1200x800', location_code: 'WMS_PALETI_BUNI', quantity: 842, state: 'GOOD' },
  { pallet_code: 'PAL-EUR-1200x800', location_code: 'WME_LINIE_AMBALARE', quantity: 136, state: 'PRODUCTION' },
  { pallet_code: 'PAL-NON-STD', location_code: 'ERP_SOLD_CLIENTI', quantity: 428, state: 'CUSTOMER' },
]

export default function Reports() {
  return (
    <section>
      <h2>Rapoarte</h2>
      <table className="table">
        <thead>
          <tr>
            <th>Palet</th>
            <th>Locatie</th>
            <th>Cantitate</th>
            <th>Stare</th>
          </tr>
        </thead>
        <tbody>
          {stock.map((item) => (
            <tr key={`${item.pallet_code}-${item.location_code}`}>
              <td>{item.pallet_code}</td>
              <td>{item.location_code}</td>
              <td>{item.quantity}</td>
              <td>{item.state}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </section>
  )
}
