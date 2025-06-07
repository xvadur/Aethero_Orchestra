import OpenAI from 'openai';

const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

export async function chatWithPremier(prompt: string, context: { role: 'user' | 'assistant' | 'system'; content: string }[] = []) {
  const messages: { role: 'user' | 'assistant' | 'system'; content: string }[] = [
    { role: 'system', content: 'You are Premier, the primary agent of AetheroOS, orchestrating Signal Root with introspective reasoning in ASL.' },
    ...context,
    { role: 'user', content: prompt },
  ];
  const response = await openai.chat.completions.create({
    model: 'gpt-4o',
    messages,
    temperature: 0.7,
    max_tokens: 1000,
  });
  return response.choices[0]?.message?.content ?? '';
}
