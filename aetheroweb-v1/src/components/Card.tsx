import { ReactNode } from 'react';

interface CardProps {
  children: ReactNode;
}

export default function Card({ children }: CardProps) {
  return (
    <div className="max-w-2xl mx-auto p-4 border border-gray-200 rounded-2xl shadow-sm bg-[#1A1B2E]">
      {children}
    </div>
  );
}
