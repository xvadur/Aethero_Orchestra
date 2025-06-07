import { useState } from 'react';
import AgentSwitcher from './AgentSwitcher';
import AgentMessage from './AgentMessage';
import { auditSummary, cognitiveMetrics } from '../lib/data';

export default function Dashboard() {
  const [auditResult, setAuditResult] = useState(null);

  const runAudit = async (threadId: string) => {
    try {
      const response = await fetch(`/api/audit/${threadId}`);
      const data = await response.json();
      setAuditResult(data);
    } catch (error) {
      console.error('Failed to run audit:', error);
    }
  };

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">AetheroOS Dashboard</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {/* System Overview */}
        <div className="border p-4 rounded-lg">
          <h2 className="text-xl font-semibold mb-2">System Overview</h2>
          <p><b>Total Aetherony:</b> {auditSummary.totalAetherony}</p>
          <p><b>Avg Aetherony/Hour:</b> {auditSummary.avgAetheronyPerHour}</p>
          <p><b>Avg Cognitive Load:</b> {auditSummary.avgCognitiveLoad}</p>
          <p><b>Avg Rhythm Score:</b> {auditSummary.avgRhythmScore}</p>
          <p><b>Most Productive Day:</b> {auditSummary.mostProductiveDay}</p>
          <p><b>Efficiency:</b> {auditSummary.efficiency}</p>
        </div>

        {/* Agent Status Panel */}
        <div className="border p-4 rounded-lg">
          <h2 className="text-xl font-semibold mb-2">Agent Status Panel</h2>
          <AgentSwitcher activeAgent="Premier" onSelect={(agent) => console.log(agent)} />
        </div>

        {/* Logs & Memory Inspector */}
        <div className="border p-4 rounded-lg">
          <h2 className="text-xl font-semibold mb-2">Logs & Memory Inspector</h2>
          <p>Memory logs will be displayed here.</p>
        </div>

        {/* AI Output Visualizer */}
        <div className="border p-4 rounded-lg">
          <h2 className="text-xl font-semibold mb-2">AI Output Visualizer</h2>
          <AgentMessage role="agent" agentName="Premier" content="Hello, world!" />
        </div>

        {/* API Playground */}
        <div className="border p-4 rounded-lg">
          <h2 className="text-xl font-semibold mb-2">API Playground</h2>
          <p>Test API endpoints here.</p>
        </div>

        {/* Run Audit */}
        <div className="border p-4 rounded-lg">
          <h2 className="text-xl font-semibold mb-2">Run Audit</h2>
          <button
            className="bg-[#00B7EB] text-white px-3 py-1 rounded font-orbitron"
            onClick={() => runAudit('exampleThreadId')}
          >
            Run Audit
          </button>
          {auditResult && (
            <div className="mt-4">
              <h3 className="text-lg font-semibold">Audit Result:</h3>
              <pre>{JSON.stringify(auditResult, null, 2)}</pre>
            </div>
          )}
        </div>

        {/* Cognitive Metrics */}
        <div className="border p-4 rounded-lg">
          <h2 className="text-xl font-semibold mb-2">Cognitive Metrics</h2>
          <ul>
            <li><b>Cognitive Coherence Rate:</b> {cognitiveMetrics.cognitiveCoherenceRate ?? 'N/A'}</li>
            <li><b>Cognitive Complexity Index:</b> {cognitiveMetrics.cognitiveComplexityIndex ?? 'N/A'}</li>
            <li><b>Mental Stability Factor:</b> {cognitiveMetrics.mentalStabilityFactor ?? 'N/A'}</li>
            <li><b>Emotional Resonance Depth:</b> {cognitiveMetrics.emotionalResonanceDepth ?? 'N/A'}</li>
            <li><b>Temporal Awareness Level:</b> {cognitiveMetrics.temporalAwarenessLevel ?? 'N/A'}</li>
            <li><b>Introspective Clarity Score:</b> {cognitiveMetrics.introspectiveClarityScore ?? 'N/A'}</li>
            <li><b>Overall Cognitive Health:</b> {cognitiveMetrics.overallCognitiveHealth ?? 'N/A'}</li>
          </ul>
        </div>
      </div>
    </div>
  );
}
