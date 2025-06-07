// LegacyDashboard.tsx
// Converted from legacy-dashboard.html <body> section
// TODO: Implement Chart.js and dynamic JS features with React hooks

export default function LegacyDashboard() {
  return (
    <>
      <header className="border-b border-[#333] bg-[#121212] sticky top-0 z-10">
        <div className="container mx-auto px-4 py-3">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-2"></div>
            <div className="text-xs text-gray-400"></div>
          </div>
        </div>
      </header>

      <main className="container mx-auto px-4 py-6">
        {/* Executive Analysis */}
        <section className="mb-8">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
            {/* Market Growth Chart */}
            <div className="data-panel rounded-lg p-4">
              {/* TODO: Chart.js Market Growth Chart */}
            </div>
            {/* Demographic Breakdown */}
            <div className="data-panel rounded-lg p-4">
              {/* TODO: Chart.js Demographic Chart */}
            </div>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-6">
            {/* Key Performance Indicators */}
            <div className="data-panel rounded-lg p-3"></div>
            <div className="data-panel rounded-lg p-3"></div>
            <div className="data-panel rounded-lg p-3"></div>
            <div className="data-panel rounded-lg p-3"></div>
          </div>
        </section>

        <hr className="section-divider" />

        {/* Deep Demographic Analysis */}
        <section className="mb-8">
          <h2 className="text-xl font-semibold mb-4">DEMOGRAPHIC DEEP DIVE</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
            <div className="data-panel rounded-lg p-4">{/* TODO: Chart.js Age by Genre Chart */}</div>
            <div className="data-panel rounded-lg p-4">{/* TODO: Chart.js Gender Preferences Chart */}</div>
            <div className="data-panel rounded-lg p-4">{/* TODO: Geographic Heatmap Preview */}</div>
          </div>
          <div className="data-panel rounded-lg mb-6 p-4">
            <div className="flex justify-between items-center mb-4"></div>
            <div className="grid grid-cols-1 md:grid-cols-4 gap-3"></div>
          </div>
        </section>

        <hr className="section-divider" />

        {/* Predictive Analytics */}
        <section className="mb-8">
          <h2 className="text-xl font-semibold mb-4 flex items-center">
            <span className="status-indicator bg-purple-700"></span>
            <span>PREDICTIVE ANALYTICS</span>
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
            <div className="data-panel rounded-lg p-4">{/* TODO: Chart.js Trend Forecast Chart */}</div>
            <div className="data-panel rounded-lg p-4">{/* TODO: Chart.js Revenue Prediction Chart */}</div>
          </div>
          <div className="data-panel rounded-lg p-4">
            <div className="flex justify-between items-center mb-3"></div>
            <div className="grid grid-cols-1 md:grid-cols-4 gap-3"></div>
          </div>
        </section>

        <hr className="section-divider" />

        {/* Genre Performance Detail */}
        <section className="mb-8">
          <h2 className="text-xl font-semibold mb-4">GENRE PERFORMANCE MATRIX</h2>
          <div className="overflow-x-auto">
            <table className="w-full data-table"></table>
          </div>
        </section>
      </main>

      <footer className="border-t border-[#333] py-4 mt-8 bg-[#1e1e1e]">
        <div className="container mx-auto px-4">
          <div className="flex flex-col md:flex-row justify-between items-center text-xs text-gray-400">
            <div className="mb-2 md:mb-0"></div>
            <div></div>
          </div>
          <div className="mt-2 text-xxs text-gray-500 text-center">
            Predictive models have 87-92% accuracy on historical data | Confidence intervals at 95%
          </div>
        </div>
      </footer>

      {/* TODO: DeepSite badge and links if needed */}
    </>
  );
}
