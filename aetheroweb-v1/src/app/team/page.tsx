export default function TeamPage() {
  return (
    <div className="min-h-screen bg-[#1A1B2E] text-gray-100 p-8 flex flex-col items-center">
      <h1 className="text-4xl font-bold mb-6 text-[#00B7EB]">Tím</h1>
      <div className="max-w-2xl w-full grid grid-cols-1 md:grid-cols-2 gap-8">
        <div className="p-6 rounded-xl bg-[#252545] border-l-4 border-[#00B7EB]">
          <h2 className="text-xl font-semibold mb-2 text-[#00B7EB]">Adam Rudavský</h2>
          <p className="mb-2">Prezident, architekt systému, hlavný koordinátor projektu AetheroOS.</p>
        </div>
        <div className="p-6 rounded-xl bg-[#252545] border-l-4 border-[#4B0082]">
          <h2 className="text-xl font-semibold mb-2 text-[#4B0082]">Frontinus</h2>
          <p className="mb-2">Minister architektúry, návrh štruktúry a komponentov webu.</p>
        </div>
        <div className="p-6 rounded-xl bg-[#252545] border-l-4 border-[#00B7EB]">
          <h2 className="text-xl font-semibold mb-2 text-[#00B7EB]">Lucius</h2>
          <p className="mb-2">Minister obsahu, tvorba textov a komunikácie.</p>
        </div>
        <div className="p-6 rounded-xl bg-[#252545] border-l-4 border-[#4B0082]">
          <h2 className="text-xl font-semibold mb-2 text-[#4B0082]">Archivus</h2>
          <p className="mb-2">Minister dokumentácie, vizuály, logá, referencie.</p>
        </div>
        <div className="p-6 rounded-xl bg-[#252545] border-l-4 border-[#00B7EB]">
          <h2 className="text-xl font-semibold mb-2 text-[#00B7EB]">Implementus</h2>
          <p className="mb-2">Minister vývoja, implementácia a nasadenie webu.</p>
        </div>
      </div>
    </div>
  );
}
