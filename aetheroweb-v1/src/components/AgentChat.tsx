'use client';

import { useState, useEffect } from 'react';
import AgentInput from './AgentInput';
import AgentMessage from './AgentMessage';
import AgentSwitcher from './AgentSwitcher';
import ThreadManager from './ThreadManager';
import { runIntrospectiveAnalysis } from '@/lib/aslParser';
import { logMemory } from '@/lib/memoryLog';
import {
  createNewThreadId,
  saveMessagesToThread,
  getMessagesForThread,
  getAllThreadIds,
  formatThreadForExport,
  Message as ThreadMessage,
} from '@/lib/threadManager';

const AGENTS = ['Premier', 'Frontinus', 'Lucius', 'Implementus', 'Archivus'];

export default function AgentChat() {
  const [activeAgent, setActiveAgent] = useState(AGENTS[0]);
  const [activeThreadId, setActiveThreadId] = useState<string>('');
  const [threads, setThreads] = useState<{ id: string; messages: ThreadMessage[] }[]>([]);
  const [loading, setLoading] = useState(false);

  // Load threads from localStorage on mount
  useEffect(() => {
    (async () => {
      const ids = await getAllThreadIds();
      if (ids.length === 0) {
        const newId = await createNewThreadId();
        setActiveThreadId(newId);
        setThreads([{ id: newId, messages: [] }]);
      } else {
        const loaded = await Promise.all(ids.map(async (id) => ({ id, messages: await getMessagesForThread(id) })));
        setActiveThreadId(ids[0]);
        setThreads(loaded);
      }
    })();
  }, []);

  // Helper to get current thread messages
  const currentThread = threads.find((t) => t.id === activeThreadId) || { id: activeThreadId, messages: [] };

  // Send message to active agent
  const handleSend = async (prompt: string, broadcast = false) => {
    setLoading(true);
    const agentsToSend = broadcast ? AGENTS : [activeAgent];
    let newThreads = [...threads];
    for (const agent of agentsToSend) {
      const thread = newThreads.find((t) => t.id === activeThreadId) || { id: activeThreadId, messages: [] };
      const userMsg: ThreadMessage = { role: 'user', content: prompt, timestamp: Date.now() };
      thread.messages.push(userMsg);
      // Prepare context for API
      const context = thread.messages
        .filter((m) => m.role === 'user' || m.role === 'agent' || m.role === 'assistant')
        .map((m) => ({
          role: m.role === 'user' ? 'user' : 'assistant',
          content: m.content,
        }));
      // Call API route with agentName
      const res = await fetch('/api/chat-with-premier', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt, context, agentName: agent }),
      });
      const data = await res.json();
      const agentMsg: ThreadMessage = { role: 'agent', agentName: agent, content: data.content, timestamp: Date.now() };
      thread.messages.push(agentMsg);
      await logMemory(prompt, data.content, undefined, activeThreadId, agent);
      await saveMessagesToThread(activeThreadId, thread.messages);
      newThreads = newThreads.map((t) => (t.id === thread.id ? thread : t));
    }
    setThreads([...newThreads]);
    setLoading(false);
  };

  // Thread management
  const handleCreateThread = async () => {
    const newId = await createNewThreadId();
    setThreads([{ id: newId, messages: [] }, ...threads]);
    setActiveThreadId(newId);
  };
  const handleSelectThread = async (id: string) => {
    setActiveThreadId(id);
  };
  const handleExportThread = (id: string) => {
    const thread = threads.find((t) => t.id === id);
    if (!thread) return;
    const md = formatThreadForExport(id, thread.messages);
    // Download as .md file
    const blob = new Blob([md], { type: 'text/markdown' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `${id}.md`;
    a.click();
    URL.revokeObjectURL(url);
  };

  // ASL analysis for current thread
  const handleAnalysis = async () => {
    const thread = threads.find((t) => t.id === activeThreadId);
    if (!thread) return;
    const pairs = [];
    for (let i = 0; i < thread.messages.length; i += 2) {
      if (
        thread.messages[i] &&
        thread.messages[i + 1] &&
        thread.messages[i].role === 'user' &&
        thread.messages[i + 1].role === 'agent'
      ) {
        pairs.push({ prompt: thread.messages[i].content, response: thread.messages[i + 1].content });
      }
    }
    const aslSummary = await runIntrospectiveAnalysis(pairs);
    await logMemory('', '', aslSummary, activeThreadId, activeAgent);
    alert('Introspective analysis completed and logged.');
  };

  return (
    <div className="flex flex-col h-[80vh] w-full max-w-2xl mx-auto bg-[#1A1B2E] p-4 rounded-xl shadow-lg">
      <ThreadManager
        activeThreadId={activeThreadId}
        onSelectThread={handleSelectThread}
        onCreateThread={handleCreateThread}
        onExportThread={handleExportThread}
        threads={threads}
      />
      <AgentSwitcher activeAgent={activeAgent} onSelect={setActiveAgent} />
      <div className="flex-1 overflow-y-auto space-y-4 mb-4">
        {currentThread.messages
          .filter((m) => m.role === 'user' || m.role === 'agent')
          .map((msg, i) => (
            <AgentMessage key={i} role={msg.role === 'assistant' ? 'agent' : msg.role} agentName={msg.agentName} content={msg.content} />
          ))}
      </div>
      <AgentInput onSend={(prompt) => handleSend(prompt, false)} disabled={loading} />
      <button
        onClick={handleAnalysis}
        className="mt-4 bg-[#00B7EB] text-white px-4 py-2 rounded-lg font-orbitron"
      >
        Run Introspective Analysis
      </button>
    </div>
  );
}
