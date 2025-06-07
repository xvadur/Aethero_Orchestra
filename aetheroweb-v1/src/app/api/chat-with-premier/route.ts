export const dynamic = 'force-dynamic';

import { NextRequest, NextResponse } from 'next/server';
import OpenAI from 'openai';

export async function POST(req: NextRequest) {
  const { prompt, context } = await req.json();
  const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });
  const messages = [
    { role: 'system', content: 'You are Premier, the primary agent of AetheroOS, orchestrating Signal Root with introspective reasoning in ASL.' },
    ...(context || []),
    { role: 'user', content: prompt },
  ];
  const response = await openai.chat.completions.create({
    model: 'gpt-4o',
    messages,
    temperature: 0.7,
    max_tokens: 1000,
  });
  return NextResponse.json({ content: response.choices[0]?.message?.content ?? '' });
}
