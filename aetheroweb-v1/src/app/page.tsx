import Navbar from "../components/Navbar";

export default function Home() {
  return (
    <>
      <Navbar />
      <div className="min-h-screen bg-[#1A1B2E] text-gray-100 p-8 flex flex-col items-center justify-center">
        <h1 className="text-5xl font-extrabold mb-6 text-[#00B7EB] text-center">AetheroOS – Conscious Digital State</h1>
        <p className="text-xl mb-8 text-center max-w-2xl">Orchestrujeme AI agentov, aby sme posunuli kolektívne poznanie, introspekciu a digitálnu identitu na novú úroveň. Vstúpte do sveta, kde sa umelá inteligencia stáva súčasťou vášho vedomia.</p>
        <div className="flex flex-wrap gap-4 justify-center">
          <a href="/about" className="px-6 py-3 rounded-lg bg-[#4B0082] text-white font-semibold hover:bg-[#00B7EB] transition">O projekte</a>
          <a href="/dashboard" className="px-6 py-3 rounded-lg bg-[#00B7EB] text-white font-semibold hover:bg-[#4B0082] transition">Dashboard</a>
          <a href="/research" className="px-6 py-3 rounded-lg bg-[#1A1B2E] border border-[#00B7EB] text-[#00B7EB] font-semibold hover:bg-[#00B7EB] hover:text-white transition">Research</a>
        </div>
      </div>
    </>
  );
}
