# ↓ glibc ベース（Debian）
FROM node:20-slim

# システムツール（必要なネイティブビルド環境）を追加
RUN apt-get update && apt-get install -y python3 make g++ && apt-get clean

WORKDIR /app

# 依存関係を先にインストール
COPY package*.json ./
RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm", "run", "dev"]