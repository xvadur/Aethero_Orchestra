import { NextResponse } from 'next/server';

export async function GET() {
  // localStorage is not available server-side; audit must be implemented client-side or via a persistent API
  return NextResponse.json({ error: 'Thread audit is not available server-side. Please implement client-side or via a persistent API.' }, { status: 501 });
}
