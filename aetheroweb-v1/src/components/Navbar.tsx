import Link from 'next/link';

export default function Navbar() {
  return (
    <nav className="w-full flex items-center justify-between px-6 py-4 bg-[#1A1B2E] border-b border-[#4B0082]">
      <div className="text-2xl font-orbitron text-[#00B7EB]">AetheroOS</div>
      <div className="flex gap-6 font-exo">
        <Link href="/">Home</Link>
        <Link href="/about">About</Link>
        <Link href="/projects">Projects</Link>
        <Link href="/team">Team</Link>
        <Link href="/contact">Contact</Link>
        <Link href="/dashboard">Dashboard</Link>
        <Link href="/research">Research</Link>
        <Link href="/agents-chat" className="text-[#00B7EB] font-bold">Agents Chat</Link>
      </div>
    </nav>
  );
}
