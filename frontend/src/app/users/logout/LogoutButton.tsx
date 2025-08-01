'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';
import { useAuth } from '@/contexts/AuthContext';
import styles from './LogoutButton.module.scss';

export default function LogoutButton() {
  const router = useRouter();
  const { setUser } = useAuth();
	const [message, setMessage] = useState('');

	const handleLogout = async () => {
		try {
			const res = await fetch('http://localhost:8000/logout', {
				method: 'POST',
				credentials: 'include',
			})

			if (!res.ok) {
        throw new Error('おっと、レスポンスが正常じゃないぞ。');
      }

			setUser(null);
			router.push('/');
		} catch (error) {
			setMessage('ログアウト失敗。');
		}	
	}

  return (
    <div className={styles.container}>
      <button onClick={handleLogout}>ログアウト</button>
      {message && <p>{message}</p>}
    </div>
  );
}