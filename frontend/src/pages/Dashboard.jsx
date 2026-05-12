import StatCard from '../components/StatCard.jsx'

const stats = [
  ['Paleti buni', 842],
  ['In productie', 136],
  ['La clienti', 428],
  ['Deteriorati', 39],
]

export default function Dashboard() {
  return (
    <section>
      <h2>Dashboard</h2>
      <div className="grid">
        {stats.map(([label, value]) => <StatCard key={label} label={label} value={value} />)}
      </div>
    </section>
  )
}
