'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';
import LoginForm from './login/LoginForm'
import CreateForm from './create/CreateForm';
import DeleteButton from './delete/DeleteButton';
import UpdateForm from './update/UpdateForm';
import UserList from './list/UserList';
import styles from './UsersPage.module.scss';

export default function UsersPage() {
  const [activeTab, setActiveTab] = useState<'login' | 'create' | 'list' | 'update' | 'delete' | null>(null);
	const router = useRouter();

  return (
    <main className={styles.container}>
      <h1 className={styles.title}>👤ユーザー機能</h1>

      {/* ナビゲーションボタン */}
      <div className={styles.buttonGroup}>
        <button onClick={() => setActiveTab('login')}>ログイン</button>
        <button onClick={() => setActiveTab('create')}>作成</button>
				<button onClick={() => setActiveTab('list')}>一覧</button>
        <button onClick={() => setActiveTab('update')}>更新</button>
				<button onClick={() => setActiveTab('delete')}>削除</button>
				<button onClick={() => router.push('/')}>ホームに戻る</button> {/* ← 追加 */}
      </div>

      {/* 表示エリア */}
      <div>
        {activeTab === 'login' && <LoginForm />}
        {activeTab === 'create' && <CreateForm />}
				{activeTab === 'list' && <UserList />}
        {activeTab === 'update' && <UpdateForm />}
				{activeTab === 'delete' && <DeleteButton />}
        {!activeTab && <p>操作を選択してください。</p>}
      </div>
    </main>
  );
}