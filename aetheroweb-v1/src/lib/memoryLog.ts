// Remove all Node.js fs/path usage. Use API call for logging.

export async function logMemory(
  prompt: string,
  response: string,
  aslSummary: string | undefined,
  threadId: string,
  agentName: string
): Promise<void> {
  // Compose log entry
  const logEntry = {
    threadId,
    agentName,
    prompt,
    response,
    aslSummary,
    timestamp: Date.now(),
  };
  try {
    await fetch('/api/memory-log', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(logEntry),
    });
  } catch (err) {
    // Optionally handle/log error
    console.error('Failed to log memory:', err);
  }
}
