interface Message {
  role: 'user' | 'agent' | 'assistant';
  agentName?: string;
  content: string;
  timestamp?: number;
}

const THREAD_PREFIX = 'aeth_chat_thread_';

export default function ThreadManager({
  activeThreadId,
  onSelectThread,
  onCreateThread,
  onExportThread,
  threads,
}: {
  activeThreadId: string;
  onSelectThread: (id: string) => void;
  onCreateThread: () => void;
  onExportThread: (id: string) => void;
  threads: { id: string; messages: Message[] }[];
}) {
  return (
    <div className="mb-4 flex gap-2 items-center">
      <button
        className="bg-[#4B0082] text-white px-3 py-1 rounded font-orbitron"
        onClick={onCreateThread}
      >
        Nové vlákno
      </button>
      <div className="flex gap-2 overflow-x-auto">
        {threads.map((thread) => (
          <button
            key={thread.id}
            onClick={() => onSelectThread(thread.id)}
            className={`px-3 py-1 rounded ${
              thread.id === activeThreadId ? 'bg-[#00B7EB] text-white' : 'bg-gray-700 text-gray-300'
            }`}
          >
            {thread.id.replace(THREAD_PREFIX, '').slice(-6)}
          </button>
        ))}
      </div>
      <button
        className="ml-2 bg-[#00B7EB] text-white px-3 py-1 rounded font-orbitron"
        onClick={() => onExportThread(activeThreadId)}
      >
        Export
      </button>
    </div>
  );
}
