// src/lib/threadManager.ts

export interface Message {
  role: 'user' | 'agent' | 'assistant';
  agentName?: string;
  content: string;
  timestamp?: number;
}

const THREAD_PREFIX = 'aeth_chat_thread_';

export async function createNewThreadId(): Promise<string> {
  const threadId = `${THREAD_PREFIX}${Date.now()}`;
  localStorage.setItem(threadId, JSON.stringify([]));
  return threadId;
}

export async function saveMessagesToThread(threadId: string, messages: Message[]): Promise<void> {
  if (!threadId || !threadId.startsWith(THREAD_PREFIX)) return;
  try {
    localStorage.setItem(threadId, JSON.stringify(messages));
  } catch (error) {
    console.error('Failed to save messages to localStorage:', error);
  }
}

export async function getMessagesForThread(threadId: string): Promise<Message[]> {
  if (!threadId || !threadId.startsWith(THREAD_PREFIX)) return [];
  try {
    const data = localStorage.getItem(threadId);
    return data ? (JSON.parse(data) as Message[]) : [];
  } catch (error) {
    console.error('Failed to retrieve or parse messages from localStorage:', error);
    return [];
  }
}

export async function getAllThreadIds(): Promise<string[]> {
  const threadIds: string[] = [];
  for (let i = 0; i < localStorage.length; i++) {
    const key = localStorage.key(i);
    if (key && key.startsWith(THREAD_PREFIX)) {
      threadIds.push(key);
    }
  }
  return threadIds;
}

export function formatThreadForExport(threadId: string, messages: Message[]): string {
  const title = threadId.replace(THREAD_PREFIX, '');
  const markdownContent = messages
    .map(
      (msg) =>
        `### ${msg.role === 'user' ? 'User Input' : (msg.agentName || 'Agent Response')}` +
        `\n${msg.content}\n`
    )
    .join('\n---\n\n');
  return `# Chat Thread Log: ${title}\n\n${markdownContent}`;
}
