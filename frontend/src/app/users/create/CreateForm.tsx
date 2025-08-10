'use client';

import { useState } from 'react';
import styles from './CreateForm.module.scss';

export default function CreateForm() {
  const [name, setName] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');
  const [createdUserId, setcreatedUserId] = useState<number | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    try {
      const res = await fetch('http://localhost:8000/users/create', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, password }),
      });

      if (!res.ok) {
        throw new Error('レスポンスが正常ではない。');
      }

      const data = await res.json();
      setMessage('作成成功！');
      setcreatedUserId(data.user_id);
    } catch {
      setMessage('作成失敗。');
    }
  };

  return (
    <form onSubmit={handleSubmit} className={styles.form}>
      <h1>ユーザー作成</h1>
      <input type="text" placeholder="名前" value={name} onChange={(e) => setName(e.target.value)} />
      <input type="password" placeholder="パスワード" value={password} onChange={(e) => setPassword(e.target.value)} />
      <button type="submit">作成</button>
      <p>{message}</p>
      {createdUserId !== null && <p>ユーザーID: {createdUserId}</p>}
    </form>
  );
}