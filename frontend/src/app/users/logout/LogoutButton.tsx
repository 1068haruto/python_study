'use client';

import { useState } from 'react';
import styles from './LogoutButton.module.scss';


export default function LogoutButton() {
	const [message, setMessage] = useState('');

	const handleLogout = async () => {
		try {
			const res = await fetch('http://localhost:8000/logout', {
				method: 'POST',
				credentials: 'include',  // ← Cookie 送信
			})

			const data = await res.json();
			setMessage(data.message);
		} catch (error) {
			setMessage('ログアウト失敗。');
		}	
	}

  return (
    <div className={styles.container}>
      <button onClick={handleLogout}>ログアウト</button>
      {message && <p>{message}</p>}
    </div>
  );
}