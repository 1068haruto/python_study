'use client';

import { useState } from 'react';
import styles from './DeleteButton.module.scss';

export default function DeleteButton() {
  const [userId, setUserId] = useState('');
  const [message, setMessage] = useState('');
  const [deletedUserId, setDeletedUserId] = useState<number | null>(null);  // 入力IDと削除成功IDの管理を分離するため

  // 削除ボタン押下時に実行
  const handleDelete = async () => {
    const res = await fetch(`http://localhost:8000/users/delete/${userId}`, {
      method: 'DELETE',
    });
    const data = await res.json();
    setMessage(data.message || '削除失敗。');
    setDeletedUserId(data.user_id);
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