import { getServerSession } from 'next-auth';
import Link from 'next/link';
import { authOptions } from './api/auth/[...nextauth]/route';

export default async function Home() {
  const session = await getServerSession(authOptions);
  return (
    <div>
      <h1>{session?.user?.email}</h1>
      <h2>Test</h2>
    </div>
  );
}
