export async function fetchCurrentUser() {
  try {
    const meRes = await fetch('http://localhost:8000/me', {
			method: 'GET',
      credentials: 'include',
    });

    if (!meRes.ok) return null;

    const user = await meRes.json();
    return user;
  } catch {
    return null;
  }
}