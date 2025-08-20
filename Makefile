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

# ディレクトリ・ファイル名との衝突回避のため
.PHONY: install freeze

# 依存関係をインストールし、lockファイルを自動更新
install: backend/requirements.lock

# requirements.txtが更新された場合、lockファイルと依存関係を自動更新するルール
backend/requirements.lock: backend/requirements.txt
	@echo "Installing dependencies from requirements.txt..."
	pip install -r backend/requirements.txt
	@echo "Freezing dependencies into requirements.lock..."
	pip freeze > backend/requirements.lock

# 手動でlockファイルを作成/更新
freeze:
	pip freeze > backend/requirements.lock