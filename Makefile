# ターゲットが使用するベースURL
BACK_URL = http://localhost:8000

# ユーザー情報
USER_NAME = testuser
USER_PASSWORD = testpassword

# Cookieを保存するファイル名
COOKIE_FILE = cookies.txt


# --------------------------------------------------------
# 認証関連の確認
# --------------------------------------------------------

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


# --------------------------------------------------------
# Python依存関係の管理
# --------------------------------------------------------

# .PHONYを使い、ファイル名との衝突を避けます
.PHONY: install freeze

# 依存関係をインストール
install:
	pip install -r backend/requirements.txt

# 現状の依存関係を書き出し
freeze:
	pip freeze > backend/requirements.lock