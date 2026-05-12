export default function MovementTable({ movements }) {
  return (
    <table className="table">
      <thead>
        <tr>
          <th>ID</th>
          <th>Tip</th>
          <th>Palet</th>
          <th>Cantitate</th>
          <th>Status</th>
        </tr>
      </thead>
      <tbody>
        {movements.map((movement) => (
          <tr key={movement.id}>
            <td>{movement.id}</td>
            <td>{movement.movement_type}</td>
            <td>{movement.pallet_code}</td>
            <td>{movement.quantity}</td>
            <td>{movement.status}</td>
          </tr>
        ))}
      </tbody>
    </table>
  )
}
