import { useEffect, useRef } from 'react';
import Chart from 'chart.js/auto';
import { aetheronUnits } from '../lib/data';

export default function MarketGrowth() {
  const chartRef = useRef<HTMLCanvasElement>(null);
  const chartInstance = useRef<Chart | null>(null);

  useEffect(() => {
    if (chartRef.current) {
      const ctx = chartRef.current.getContext('2d');
      if (ctx) {
        const labels = aetheronUnits.map(unit => unit.timestamp);
        const data = aetheronUnits.map(unit => unit.value);
        chartInstance.current = new Chart(ctx, {
          type: 'bar',
          data: {
            labels,
            datasets: [{
              label: 'Aetherony Value',
              data,
              backgroundColor: '#00B7EB',
              borderColor: '#4B0082',
              borderWidth: 1
            }]
          },
          options: {
            scales: {
              y: {
                beginAtZero: true,
                title: { display: true, text: 'Aetherony Value' }
              }
            },
            plugins: {
              legend: { display: true, position: 'top' },
              title: { display: true, text: 'Aetherony Productivity Over Time' }
            }
          }
        });
      }
    }
    return () => {
      chartInstance.current?.destroy();
    };
  }, []);

  return (
    <div className="max-w-2xl mx-auto p-4 border border-[#4B0082] rounded-2xl bg-[#2A2B3E]">
      <h3 className="text-sm font-orbitron mb-2">AETHERONY PRODUCTIVITY OVER TIME</h3>
      <canvas ref={chartRef}></canvas>
    </div>
  );
}
