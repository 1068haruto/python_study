'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';
import { useAuth } from '@/contexts/AuthContext';
import { fetchCurrentUser } from '@/lib/fetchCurrentUser';
import styles from './LoginForm.module.scss';

export default function LoginForm() {
  const router = useRouter();
  const [name, setName] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');
  const { setUser } = useAuth();

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();

    try {
      const loginRes = await fetch('http://localhost:8000/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, password }),
        credentials: 'include',
      });

      if (!loginRes.ok) {
        throw new Error('レスポンスが正常ではない。');
      }

      const me = await fetchCurrentUser();
      if (!me) {
        throw new Error('認証が失敗している。');
      }

      setUser(me);
      router.push('/users');
    } catch (error) {
      setMessage('ログイン失敗。');
    }
  };

  return (
    <form onSubmit={handleLogin} className={styles.form}>
      <h1>ログイン</h1>
      <input type="text" placeholder="ユーザー名" value={name} onChange={(e) => setName(e.target.value)} />
      <input type="password" placeholder="パスワード" value={password} onChange={(e) => setPassword(e.target.value)} />
      <button type="submit">ログイン</button>
      {message && <p>{message}</p>}
    </form>
  );
}