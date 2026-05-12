import { useState } from 'react'
import Dashboard from './pages/Dashboard.jsx'
import PalletMovements from './pages/PalletMovements.jsx'
import Reports from './pages/Reports.jsx'

const pages = {
  dashboard: Dashboard,
  movements: PalletMovements,
  reports: Reports,
}

export default function App() {
  const [page, setPage] = useState('dashboard')
  const Page = pages[page]

  return (
    <main className="app-shell">
      <header className="app-header">
        <div>
          <p className="eyebrow">MVP skeleton</p>
          <h1>TraceAI Control - Gestionare Paleti</h1>
          <p>Demo UI pentru control paleti ERP / WMS / WME.</p>
        </div>
        <nav>
          <button onClick={() => setPage('dashboard')}>Dashboard</button>
          <button onClick={() => setPage('movements')}>Miscari</button>
          <button onClick={() => setPage('reports')}>Rapoarte</button>
        </nav>
      </header>
      <Page />
    </main>
  )
}
