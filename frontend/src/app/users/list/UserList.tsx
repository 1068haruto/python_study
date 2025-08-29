'use client';

import { useEffect, useState } from 'react';
import styles from './UserList.module.scss';
import DeleteButton from '@/app/users/delete/DeleteButton';

type User = {
  id: number;
  name: string;
};

export default function UserList() {
  const [users, setUsers] = useState<User[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchUsers = async () => {
      try {
        const res = await fetch('http://localhost:8000/users/list');

        if (!res.ok) {
          throw new Error('ユーザー一覧の取得に失敗。');
        }

        const data = await res.json();
        setUsers(data);
      } catch (err: any) {
        setError(err.message);
      } finally {
        setIsLoading(false);
      }
    };

    fetchUsers();
  }, []);

  // 削除成功時
  const handleUserDeleteSuccess = (deletedId: number) => {
    // エラーメッセージをクリア
    setError(null);
    // リストから削除済ユーザーを除外
    setUsers(prevUsers => prevUsers.filter(user => user.id !== deletedId));
  };

  // 削除失敗時
  const handleUserDeleteError = (errorMessage: string) => {
    setError(errorMessage);
  };

  if (isLoading) {
    return <p>読み込み中...</p>;
  }

  return (
    <div className={styles.list}>
      <h1>ユーザー一覧</h1>
      <ul>
        {users.map(user => (
          <li key={user.id}>
            <span>ユーザーID: {user.id} / 名前: {user.name}</span>
            <DeleteButton
              userId={user.id}
              onDeleteSuccess={handleUserDeleteSuccess}
              onDeleteError={handleUserDeleteError}
            />
          </li>
        ))}
        {error && <p>{error}</p>}
      </ul>
    </div>
  );
}