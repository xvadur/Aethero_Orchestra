export async function fetchAnalytics() {
  // Mockované dáta, nahradiť OpenAI API alebo AetheroOS endpointom
  return {
    marketShare: { value: '17.2%', growth: '+3.4% YoY' },
    revenuePerUser: { value: '$3.42', growth: '+11.1% YoY' },
    demographic: { age: '25-34', percent: '42%' },
    genreTop: { name: 'Sci-Fi', percent: '28%' },
    churnPrediction: { value: '4.2%', trend: 'klesajúci' },
  };
}
