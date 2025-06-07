'use client';

import MarketGrowth from '@/components/MarketGrowth';
import Demographics from '@/components/Demographics';
import PredictiveAnalytics from '@/components/PredictiveAnalytics';
import GenreMatrix from '@/components/GenreMatrix';
import AgentChat from '@/components/AgentChat';

export default function Dashboard() {
  return (
    <div className="bg-[#1A1B2E] min-h-screen text-white font-exo">
      <header className="border-b border-[#4B0082] bg-[#121212] sticky top-0 z-10 py-4">
        <div className="container mx-auto px-4">
          <h1 className="text-lg font-orbitron text-[#00B7EB]">
            AETHEROOS ANALYTICS v1.0
          </h1>
          <p className="text-xs text-gray-400">Last updated: 2025-06-07 | Data source: AetheroOS API</p>
        </div>
      </header>

      <main className="container mx-auto px-4 py-6">
        <section className="mb-8">
          <h2 className="text-xl font-orbitron mb-4">EXECUTIVE ANALYSIS</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
            <MarketGrowth />
            <Demographics />
          </div>
          <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
            {/* KPIs and additional cards can be added here */}
          </div>
        </section>

        <hr className="border-[#4B0082] my-6" />

        <section className="mb-8">
          <h2 className="text-xl font-orbitron mb-4">DEMOGRAPHIC DEEP DIVE</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            {/* Demographic charts/components */}
          </div>
        </section>

        <hr className="border-[#4B0082] my-6" />

        <section className="mb-8">
          <h2 className="text-xl font-orbitron mb-4">PREDICTIVE ANALYTICS</h2>
          <PredictiveAnalytics />
        </section>

        <hr className="border-[#4B0082] my-6" />

        <section className="mb-8">
          <h2 className="text-xl font-orbitron mb-4">GENRE PERFORMANCE MATRIX</h2>
          <GenreMatrix />
        </section>

        <section className="mb-8">
          <h2 className="text-xl font-orbitron mb-4">AGENT INTERACTION</h2>
          <AgentChat />
        </section>
      </main>

      <footer className="border-t border-[#4B0082] py-4 bg-[#121212] text-center">
        <p className="text-xs text-gray-400">AetheroOS Analytics | Powered by Signal Root</p>
      </footer>
    </div>
  );
}
