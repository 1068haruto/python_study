'use client'

import Link from 'next/link';
import styles from './page.module.scss';

export default function Home() {
  return (
    <main className={styles.container}>
      <h1 className={styles.title}>🏠ホーム</h1>

      {/* ナビゲーションボタン */}
      <div className={styles.buttonGroup}>
        <Link href="/users">ユーザー機能</Link>
      </div>
    </main>
  );
}