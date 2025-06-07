import { useEffect, useRef } from 'react';
import Chart from 'chart.js/auto';

export default function PredictiveAnalytics() {
  const chartRef = useRef<HTMLCanvasElement>(null);
  const chartInstance = useRef<Chart | null>(null);

  useEffect(() => {
    if (chartRef.current) {
      const ctx = chartRef.current.getContext('2d');
      if (ctx) {
        chartInstance.current = new Chart(ctx, {
          type: 'line',
          data: {
            labels: ['2022', '2023', '2024', '2025', '2026'],
            datasets: [{
              label: 'Revenue Forecast ($M)',
              data: [2.1, 2.4, 2.8, 3.2, 3.7],
              backgroundColor: '#00B7EB',
              borderColor: '#00B7EB',
              tension: 0.4,
              fill: false
            }]
          },
          options: {
            scales: {
              y: {
                beginAtZero: true,
                title: { display: true, text: 'Revenue ($M)' }
              }
            },
            plugins: {
              legend: { display: true, position: 'top' },
              title: { display: true, text: 'Predictive Revenue Analytics' }
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
      <h3 className="text-sm font-orbitron mb-2">PREDICTIVE ANALYTICS</h3>
      <canvas ref={chartRef}></canvas>
    </div>
  );
}
