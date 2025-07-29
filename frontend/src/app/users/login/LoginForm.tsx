'use client';

import { useState } from 'react';
import styles from './LoginForm.module.scss';

export default function LoginForm() {
  const [name, setName] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();

    try {
      const loginRes = await fetch('http://localhost:8000/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, password }),
        credentials: 'include', // ← Cookie送信
      });

      if (!loginRes.ok) throw new Error('ログイン失敗');

      const meRes = await fetch('http://localhost:8000/me', {
        method: 'GET',
        credentials: 'include', // ← Cookie送信
      });

      if (!meRes.ok) throw new Error('認証失敗');

      const me = await meRes.json();
      setMessage(`ログイン成功！こんにちは ${me.name} さん`);
    } catch (err) {
      setMessage('ログインに失敗した。');
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