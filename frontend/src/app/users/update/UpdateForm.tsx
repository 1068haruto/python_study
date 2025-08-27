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

    const isNameEmpty = name.trim() === '';
    const isPasswordEmpty = password.trim() === '';

    // 未入力で送信された場合、クライアント側で処理を止める
    if (isNameEmpty && isPasswordEmpty) {
      setMessage('更新なし。');
      setUpdatedUserId(null);
      return;
    }

    try {
      const body: any = {};
      // rim()で、空白文字だけのデータ送信を防止
      if (name.trim() !== '') body.name = name;
      if (password.trim() !== '') body.password = password;

      const res = await fetch(`http://localhost:8000/users/update/${userId}`, {
 	  	  method: 'PUT',
    	  headers: { 'Content-Type': 'application/json' },
    	  body: JSON.stringify(body),
  	  });

      // 200台以外の場合
      if (!res.ok) {
        if (res.status === 404) {
          setMessage('ユーザーが見つからない。');
        } else {
          setMessage('未定義のエラーが発生。');
        }
        setUpdatedUserId(null);
        return;
      }

      // 200台の場合
      const data = await res.json();
      if (data.updated) {
        setMessage('更新成功！');
        setUpdatedUserId(data.user_id);
      } else {
        setMessage('更新なし。');
        setUpdatedUserId(data.user_id);
      }
    } catch {
      setMessage('更新失敗。');
      setUpdatedUserId(null);
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