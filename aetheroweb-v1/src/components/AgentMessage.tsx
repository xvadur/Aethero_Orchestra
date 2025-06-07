interface AgentMessageProps {
  role: 'user' | 'agent';
  agentName?: string;
  content: string;
}

export default function AgentMessage({ role, agentName, content }: AgentMessageProps) {
  let borderColor = '';
  if (role === 'agent') {
    switch (agentName) {
      case 'Premier':
        borderColor = 'border-[#00B7EB]';
        break;
      case 'Frontinus':
        borderColor = 'border-[#4B0082]';
        break;
      case 'Lucius':
        borderColor = 'border-green-400';
        break;
      case 'Implementus':
        borderColor = 'border-yellow-400';
        break;
      case 'Archivus':
        borderColor = 'border-pink-400';
        break;
      default:
        borderColor = 'border-gray-500';
    }
  }
  return (
    <div
      className={`p-3 rounded-lg max-w-[80%] font-exo ${
        role === 'user'
          ? 'bg-[#4B0082] text-white ml-auto'
          : `bg-[#2A2B3E] text-[#00B7EB] mr-auto border-l-4 ${borderColor}`
      }`}
    >
      {role === 'agent' && agentName && (
        <div className="text-xs font-bold mb-1 uppercase tracking-wider opacity-80">{agentName}</div>
      )}
      {content}
    </div>
  );
}
