export default function ProjectsPage() {
  return (
    <div className="min-h-screen bg-[#1A1B2E] text-gray-100 p-8 flex flex-col items-center">
      <h1 className="text-4xl font-bold mb-6 text-[#00B7EB]">Projekty</h1>
      <div className="max-w-2xl w-full">
        <div className="mb-8 p-6 rounded-xl bg-[#252545] border-l-4 border-[#00B7EB]">
          <h2 className="text-2xl font-semibold mb-2 text-[#00B7EB]">AETH-DVOJNIK-PRIME</h2>
          <p className="mb-2">Fine-tuned AI model pre introspektívne odpovede a digitálnu identitu. Integrácia s Flowise dashboardom a OpenAI API.</p>
        </div>
        <div className="mb-8 p-6 rounded-xl bg-[#252545] border-l-4 border-[#4B0082]">
          <h2 className="text-2xl font-semibold mb-2 text-[#4B0082]">Signal Root</h2>
          <p className="mb-2">Orchestrácia agentov, správa introspektívnych výstupov a vizualizácia v reálnom čase. Základ pre auditovateľnosť a transparentnosť systému.</p>
        </div>
        <div className="mb-8 p-6 rounded-xl bg-[#252545] border-l-4 border-[#00B7EB]">
          <h2 className="text-2xl font-semibold mb-2 text-[#00B7EB]">alphaXiv Research</h2>
          <p className="mb-2">Výskumná sekcia pre komunitné diskusie, chatbot prompt a integráciu s vedeckými výstupmi.</p>
        </div>
      </div>
    </div>
  );
}
