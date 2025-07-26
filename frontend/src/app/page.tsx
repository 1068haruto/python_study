import Link from 'next/link';
import styles from './page.module.scss';

export default function Home() {
  return (
    <main className={styles.main}>
      <h1>Home</h1>
      <p>ユーザーの作成と削除ができる</p>

      <div className={styles.links}>
        <Link href="/users/list"><button>ユーザー一覧</button></Link>
        <Link href="/users/create"><button>ユーザー作成</button></Link>
        <Link href="/users/delete"><button>ユーザー削除</button></Link>
      </div>
    </main>
  );
}