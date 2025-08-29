'use client';

import { useState } from 'react';
import styles from './DeleteButton.module.scss';

// 親からuserIdと削除成功時のコールバック関数を受け取る
type DeleteButtonProps = {
  userId: number;
  onDeleteSuccess: (deletedId: number) => void;
  onDeleteError: (error: string) => void;
};

export default function DeleteButton({ userId, onDeleteSuccess, onDeleteError }: DeleteButtonProps) {
  const [isDeleting, setIsDeleting] = useState(false);

  const handleDelete = async () => {
    setIsDeleting(true);

    try {
      const res = await fetch(`http://localhost:8000/users/delete/${userId}`, {
        method: 'DELETE',
      });

      if (!res.ok) {
        throw new Error('削除リクエストに失敗。');
      }

      onDeleteSuccess(userId);    // 成功時：親に成功を通知
    } catch (err: any) {
      onDeleteError(err.message); // 失敗時：親にエラーを通知
    } finally {
      setIsDeleting(false);
    }
  };

  return (
    <div>
      <button onClick={handleDelete} disabled={isDeleting} className={styles.button}>
        {isDeleting ? '削除中...' : '削除'}
      </button>
    </div>
  );
}