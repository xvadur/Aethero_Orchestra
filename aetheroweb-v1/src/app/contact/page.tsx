export default function ContactPage() {
  return (
    <div className="min-h-screen bg-[#1A1B2E] text-gray-100 p-8 flex flex-col items-center">
      <h1 className="text-4xl font-bold mb-6 text-[#00B7EB]">Kontakt</h1>
      <div className="max-w-xl w-full bg-[#252545] rounded-xl p-8 border-l-4 border-[#00B7EB]">
        <p className="mb-4">Pre spoluprácu, otázky alebo mediálne dopyty nás kontaktujte:</p>
        <ul className="mb-4">
          <li className="mb-2"><span className="font-semibold">E-mail:</span> <a href="mailto:info@aetheroos.com" className="text-[#00B7EB] underline">info@aetheroos.com</a></li>
          <li className="mb-2"><span className="font-semibold">GitHub:</span> <a href="https://github.com/xvadur/Aethero_github" className="text-[#00B7EB] underline" target="_blank">AetheroOS / Aethero Labs</a></li>
        </ul>
        <p className="text-sm text-gray-400">AetheroOS je otvorený projekt. Pridajte sa k nám na ceste za digitálnou introspekciou!</p>
      </div>
    </div>
  );
}
