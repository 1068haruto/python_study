'use client';

import { useAuth } from '@/contexts/AuthContext';
import styles from './UserStatus.module.scss';

export default function UserStatus() {
  const { user } = useAuth();

  return user ? (
    <p className={`${styles.status} ${styles.loggedIn}`}>
      こんにちは {user.name} さん
    </p>
  ) : (
    <p className={`${styles.status} ${styles.loggedOut}`}>
      ログインしていません
    </p>
  );
}