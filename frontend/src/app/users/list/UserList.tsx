'use client';

import { useEffect, useState } from 'react';
import styles from './UserList.module.scss';

type User = {
  id: number;
  name: string;
};

export default function UserList() {
  const [users, setUsers] = useState<User[]>([]);

  useEffect(() => {
    fetch('http://localhost:8000/users/list')
      .then(res => res.json())
      .then(data => setUsers(data));
    },[]
	);

  return (
    <div className={styles.list}>
      <h1>ユーザー一覧</h1>
      <ul>
        {users.map(user => (
          <li key={user.id}>
            ユーザーID: {user.id} / 名前: {user.name}
          </li>
        ))}
      </ul>
    </div>
  );
}