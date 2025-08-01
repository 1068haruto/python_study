'use client'

import { useState } from 'react';
import Link from 'next/link';
import LoginForm from './users/login/LoginForm'
import styles from './page.module.scss';

export default function Home() {
  const [activeTab, setActiveTab] = useState<'login' | null>(null);

  return (
    <main className={styles.container}>
      <h1 className={styles.title}>🏠ホーム</h1>

      {/* ナビゲーションボタン */}
      <div className={styles.buttonGroup}>
        <button onClick={() => setActiveTab('login')}>ログイン</button>
        <Link href="/users">ユーザー機能</Link>
      </div>

      {/* 表示エリア */}
        <div>
          {activeTab === 'login' && <LoginForm />}
        </div>
    </main>
  );
}