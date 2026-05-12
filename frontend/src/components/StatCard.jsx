export default function StatCard({ label, value }) {
  return (
    <section className="stat-card">
      <p>{label}</p>
      <strong>{value}</strong>
    </section>
  )
}
