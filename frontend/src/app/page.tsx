import Link from 'next/link';
import styles from './page.module.scss';

export default function Home() {
  return (
    <main className={styles.main}>
      <h1>Home</h1>
      <p>ユーザーの作成と削除ができる</p>

      <div className={styles.links}>
        <Link href="/users/list"><button>一覧ページ</button></Link>
        <Link href="/users/create"><button>作成ページ</button></Link>
        <Link href="/users/update"><button>更新ページ</button></Link>
        <Link href="/users/delete"><button>削除ページ</button></Link>
      </div>
    </main>
  );
}