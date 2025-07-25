from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import user  # ルーターの読み込み

app = FastAPI()

# CORSの設定を追加
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # ftontアプリのURLを許可
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ルーターの登録
app.include_router(user.router)

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI from Docker!"}