export default function ResearchPage() {
  return (
    <div className="min-h-screen bg-[#1A1B2E] text-gray-100 p-8 flex flex-col items-center">
      <h1 className="text-4xl font-bold mb-6 text-[#00B7EB]">Research & alphaXiv</h1>
      <div className="max-w-2xl w-full bg-[#252545] rounded-xl p-8 border-l-4 border-[#4B0082]">
        <p className="mb-4">Zapojte sa do výskumných diskusií, experimentov a komunitných projektov v rámci AetheroOS. Sledujte najnovšie výstupy, publikácie a pripojte sa k alphaXiv diskusiám.</p>
        <a href="https://alphaxiv.org" target="_blank" className="inline-block mt-4 px-6 py-3 rounded-lg bg-[#00B7EB] text-white font-semibold hover:bg-[#4B0082] transition">Prejsť na alphaXiv</a>
      </div>
    </div>
  );
}
