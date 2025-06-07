const agents = ['Premier', 'Frontinus', 'Lucius', 'Implementus', 'Archivus'];

interface AgentSwitcherProps {
  activeAgent: string;
  onSelect: (agent: string) => void;
}

export default function AgentSwitcher({ activeAgent, onSelect }: AgentSwitcherProps) {
  return (
    <div className="flex border-b border-[#4B0082] mb-4">
      {agents.map((agent) => (
        <button
          key={agent}
          onClick={() => onSelect(agent)}
          className={`px-4 py-2 font-orbitron ${
            activeAgent === agent ? 'text-[#00B7EB] border-b-2 border-[#00B7EB]' : 'text-gray-400'
          }`}
        >
          {agent}
        </button>
      ))}
    </div>
  );
}
