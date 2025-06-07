export default function AboutPage() {
  return (
    <div className="min-h-screen bg-[#1A1B2E] text-gray-100 p-8 flex flex-col items-center">
      <h1 className="text-4xl font-bold mb-6 text-[#00B7EB]">O projekte AetheroOS</h1>
      <p className="max-w-2xl text-lg mb-4 text-center">
        AetheroOS je experimentálny operačný systém novej generácie, ktorý prepája introspektívnu umelú inteligenciu, orchestráciu agentov a digitálnu identitu. Naším cieľom je vytvoriť platformu, kde AI agenti spolupracujú na riešení komplexných úloh, analyzujú dáta v reálnom čase a podporujú kolektívne poznanie.
      </p>
      <p className="max-w-2xl text-lg mb-4 text-center">
        Technologický stack: OpenAI SDKs, LangChain, Flowise, CrewAI, Next.js, TailwindCSS, Python, TypeScript.
      </p>
      <p className="max-w-2xl text-lg mb-4 text-center">
        AetheroOS je otvorený projekt, ktorý podporuje transparentnosť, auditovateľnosť a komunitnú spoluprácu.
      </p>
    </div>
  );
}
