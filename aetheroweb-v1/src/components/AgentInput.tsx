import { useState } from 'react';

interface AgentInputProps {
  onSend: (prompt: string) => void;
  disabled: boolean;
}

export default function AgentInput({ onSend, disabled }: AgentInputProps) {
  const [prompt, setPrompt] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (prompt.trim()) {
      onSend(prompt);
      setPrompt('');
    }
  };

  return (
    <form onSubmit={handleSubmit} className="flex gap-2">
      <textarea
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        className="flex-1 p-2 rounded-lg bg-[#2A2B3E] text-white border border-[#4B0082] font-exo"
        placeholder="Enter your prompt..."
        disabled={disabled}
      />
      <button
        type="submit"
        className="bg-[#00B7EB] text-white px-4 py-2 rounded-lg font-orbitron"
        disabled={disabled}
      >
        Send
      </button>
    </form>
  );
}
