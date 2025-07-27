import Link from 'next/link';
import styles from './page.module.scss';

export default function Home() {
  return (
    <main className={styles.main}>
      <h1 className={styles.title}>🏠ホーム</h1>
      <p>機能を選択</p>
      <div className={styles.links}>
        <Link href="/users" className={styles.linkButton}>ユーザー機能</Link>
      </div>
    </main>
  );
}