'use client';

import { useSession } from 'next-auth/react';
import Link from 'next/link';

export default function Header() {
  const { status, data: session } = useSession();
  return (
    <div className='w-full absolute z-10'>
      <nav className='contaienr relative flex flex-wrap items-center justify-between mx-auto p-8'>
        <Link href='/' className='font-bond text-3xl'>
          Home
        </Link>
        <div className='space-x-4 text-xl'>
          {status === 'loading' && <div>loading...</div>}
          {status === 'authenticated' && (
            <div className='mr-3'>
              {session.user!.name}
              <Link href='/api/auth/signout' className='ml-3'>
                Sign Out
              </Link>
            </div>
          )}
          {status === 'unauthenticated' && (
            <Link href='/api/auth/signin'>Login</Link>
          )}
          <Link href='/about'>About</Link>
          <Link href='/user'>User</Link>
        </div>
      </nav>
    </div>
  );
}
