'use client';

import { useState } from 'react';
import styles from './UpdateForm.module.scss';

export default function UpdateForm() {
  const [userId, setUserId] = useState('');
  const [name, setName] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');
  const [updatedUserId, setUpdatedUserId] = useState<number | null>(null);

	const handleSubmit = async (e: React.FormEvent) => {
  	e.preventDefault();

    try {
      const body: any = {};
  	  if (name !== '') body.name = name;
   	  if (password !== '') body.password = password;

      const res = await fetch(`http://localhost:8000/users/update/${userId}`, {
 	  	  method: 'PUT',
    	  headers: { 'Content-Type': 'application/json' },
    	  body: JSON.stringify(body),
  	  });

      if (!res.ok) {
        throw new Error('レスポンスが正常ではない。');
      }

      const data = await res.json();
      setMessage('更新成功！');
      setUpdatedUserId(data.user_id);
    } catch {
      setMessage('更新失敗。');
    }
	};

  return (
    <form onSubmit={handleSubmit} className={styles.form}>
      <h1>ユーザー更新</h1>
      <input type="number" placeholder="ユーザーID" value={userId} onChange={(e) => setUserId(e.target.value)} />
      <input type="text" placeholder="新しい名前" value={name} onChange={(e) => setName(e.target.value)} />
      <input type="password" placeholder="新しいパスワード" value={password} onChange={(e) => setPassword(e.target.value)} />
      <button type="submit">更新</button>
      <p>{message}</p>
      {updatedUserId !== null && <p>更新されたユーザーID: {updatedUserId}</p>}
    </form>
  );
}