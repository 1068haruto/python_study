'use client';

import { useState } from 'react';
import styles from './DeleteButton.module.scss';

export default function DeleteButton() {
  const [userId, setUserId] = useState('');
  const [message, setMessage] = useState('');
  const [deletedUserId, setDeletedUserId] = useState<number | null>(null);  // 入力IDと削除成功IDの管理を分離するため

  const handleDelete = async () => {
    try {
      const res = await fetch(`http://localhost:8000/users/delete/${userId}`, {
        method: 'DELETE',
      });

      if (!res.ok) {
        throw new Error('レスポンスが正常ではない。');
      }

      const data = await res.json();
      setMessage('削除成功！');
      setDeletedUserId(data.user_id);
    } catch {
      setMessage('削除失敗。');
    }
  };

  return (
    <div className={styles.container}>
      <h1>ユーザー削除</h1>
      <input type="number" placeholder="削除するユーザーID" value={userId} onChange={(e) => setUserId(e.target.value)} />
      <button onClick={handleDelete}>削除</button>
      <p>{message}</p>
      {deletedUserId !== null && <p>ユーザーID: {deletedUserId}</p>}
    </div>
  );
}