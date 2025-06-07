import { NextResponse } from 'next/server';
import fs from 'fs/promises';
import path from 'path';

export async function POST(request: Request) {
  const logEntry = await request.json();
  const logsDir = path.join(process.cwd(), 'logs/MemoryLogs');
  const logPath = path.join(logsDir, `log_${new Date().toISOString().split('T')[0]}.json`);
  // Ensure directory exists
  await fs.mkdir(logsDir, { recursive: true });
  await fs.appendFile(logPath, JSON.stringify(logEntry) + '\n');
  return NextResponse.json({ status: 'Logged' });
}
