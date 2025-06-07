// Real audit data for dashboard analytics (Aethero)
export const auditSummary = {
  totalAetherony: 7.41,
  avgAetheronyPerHour: 1.85,
  avgCognitiveLoad: 6.13,
  avgRhythmScore: 0.45,
  mostProductiveDay: '2025-06-01',
  productivityByDay: {
    '2025-06-01': 4.71,
    '2025-06-04': 2.70
  },
  topPatterns: { debugging: 3 },
  efficiency: 'Vysoká - Efektívny Solo Developer 💪'
};

export const sessionData = [
  {
    start: '2025-06-01T08:22:07',
    end: '2025-06-01T10:59:31',
    duration: 2.62,
    commits: 19,
    aetherony: 9.5,
    cognitiveCoherence: 0.57,
    productivity: 'vysoká'
  },
  {
    start: '2025-06-04T01:32:01',
    end: '2025-06-04T02:39:43',
    duration: 1.13,
    commits: 3,
    aetherony: 1.5,
    cognitiveCoherence: 0.30,
    productivity: 'stredná'
  },
  {
    start: '2025-06-04T08:14:41',
    end: '2025-06-04T08:39:41',
    duration: 0.42,
    commits: 6,
    aetherony: 3.0,
    cognitiveCoherence: 0.50,
    productivity: 'vysoká'
  }
];

export const aetheronUnits = [
  {
    timestamp: '2025-06-01T08:22:07',
    value: 3.09,
    commits: 7,
    shell: 0,
    cognitiveLoad: 5.45,
    rhythm: 0.7,
    efficiency: 0.40,
    tags: ['debugging']
  },
  {
    timestamp: '2025-06-01T09:22:07',
    value: 1.61,
    commits: 4,
    shell: 0,
    cognitiveLoad: 5.45,
    rhythm: 0.4,
    efficiency: 0.23,
    tags: ['debugging']
  },
  {
    timestamp: '2025-06-04T01:32:01',
    value: 0.70,
    commits: 2,
    shell: 0,
    cognitiveLoad: 7.6,
    rhythm: 0.2,
    efficiency: 0.06,
    tags: ['debugging']
  },
  {
    timestamp: '2025-06-04T08:14:41',
    value: 2.0,
    commits: 5,
    shell: 0,
    cognitiveLoad: 6.0,
    rhythm: 0.5,
    efficiency: 0.25,
    tags: []
  }
];

// Deprecated: For legacy compatibility only. Use auditSummary/sessionData/aetheronUnits instead.
export const comicData = {};

// Placeholder for cognitive metrics (to be filled with real values from cognitive analysis pipeline)
export const cognitiveMetrics = {
  // Example structure, replace with real values if available
  cognitiveCoherenceRate: 0.57, // session average or most recent
  cognitiveComplexityIndex: null, // not present in audit, add if available
  mentalStabilityFactor: null,
  emotionalResonanceDepth: null,
  temporalAwarenessLevel: null,
  introspectiveClarityScore: null,
  overallCognitiveHealth: null
};
