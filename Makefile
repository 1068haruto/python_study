# ターゲットが使用するベースURL
BACK_URL = http://localhost:8000

# ユーザー情報
USER_NAME = testuser
USER_PASSWORD = testpassword

# Cookieを保存するファイル名
COOKIE_FILE = cookies.txt


# 認証関連の確認 -----------------------------------------------------------

# ログイン（cookies.txtにCookieを保存）
login:
	@curl -X POST $(BACK_URL)/login \
		-H "Content-Type: application/json" \
		-d '{"name": "$(USER_NAME)", "password": "$(USER_PASSWORD)"}' \
		-c $(COOKIE_FILE)

# ログアウト（cookies.txtをクリア）
logout:
	@curl -X POST $(BACK_URL)/logout -b $(COOKIE_FILE) -c $(COOKIE_FILE)

# ユーザー認証（tokenありの状態）
check_auth:
	@curl -X GET $(BACK_URL)/me -b $(COOKIE_FILE)

# ユーザー認証（tokenなしの状態）
check_auth_no_token:
	@curl -X GET $(BACK_URL)/me