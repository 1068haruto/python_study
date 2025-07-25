'use client';

import { useState } from 'react';
import styles from './CreateForm.module.scss';

export default function CreateForm() {
  // 状態管理
  const [name, setName] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');

  // フォーム送信時に実行
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const res = await fetch('http://localhost:8000/users/create', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name, password }),
    });
    const data = await res.json();
    setMessage(data.message);
  };

  return (
    <form onSubmit={handleSubmit} className={styles.form}>
      <h1>ユーザー作成</h1>
      <input type="text" placeholder="名前" value={name} onChange={(e) => setName(e.target.value)} />
      <input type="password" placeholder="パスワード" value={password} onChange={(e) => setPassword(e.target.value)} />
      <button type="submit">作成</button>
      <p>{message}</p>
    </form>
  );
}