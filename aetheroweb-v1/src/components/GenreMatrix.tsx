import { aetheronUnits } from '../lib/data';

export default function GenreMatrix() {
  return (
    <div className="overflow-x-auto max-w-4xl mx-auto p-4 border border-[#4B0082] rounded-2xl bg-[#2A2B3E]">
      <h3 className="text-sm font-orbitron mb-2">AETHERON UNIT METRICS</h3>
      <table className="min-w-full data-table">
        <thead>
          <tr>
            <th>Timestamp</th>
            <th>Value</th>
            <th>Commits</th>
            <th>Cognitive Load</th>
            <th>Rhythm</th>
            <th>Efficiency</th>
            <th>Tags</th>
          </tr>
        </thead>
        <tbody>
          {aetheronUnits.map((unit, idx) => (
            <tr key={idx}>
              <td>{unit.timestamp}</td>
              <td>{unit.value}</td>
              <td>{unit.commits}</td>
              <td>{unit.cognitiveLoad}</td>
              <td>{unit.rhythm}</td>
              <td>{unit.efficiency}</td>
              <td>{unit.tags.join(', ')}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
