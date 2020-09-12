from typing import List, Optional  # ネストされたBodyを定義するために必要

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware  # CORSを回避するために必要

from app.db import session  # DBと接続するためのセッション
from app.model import User, UserDdb, UserTable  # 今回使うモデルをインポート


app = FastAPI()

# CORSを回避するために設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ----------APIの定義------------
# テーブルにいる全ユーザ情報を取得 GET
@app.get("/users")
def read_users():
    users = session.query(UserTable).all()
    return users


@app.get("/users_ddb")
def read_users_ddb():
    users = UserDdb.scan()
    return users


# idにマッチするユーザ情報を取得 GET
@app.get("/users/{user_id}")
def read_user(user_id: int):
    user = session.query(UserTable).filter(UserTable.id == user_id).first()
    return user


# ユーザ情報を登録 POST
@app.post("/user")
# クエリでnameとstrを受け取る
# /user?name="三郎"&age=10
async def create_user(name: str, age: int):
    user = UserTable()
    user.name = name
    user.age = age
    session.add(user)
    session.commit()


# ユーザ情報を登録 POST
@app.post("/user_ddb")
# クエリでnameとstrを受け取る
# /user?name="三郎"&age=10
async def create_user_ddb(id: int, name: str, age: Optional[int] = None):
    user = UserDdb()
    user.id = id
    user.name = name
    if age:
        user.age = age
    user.save()


# 複数のユーザ情報を更新 PUT
@app.put("/users")
# modelで定義したUserモデルのリクエストbodyをリストに入れた形で受け取る
# users=[{"id": 1, "name": "一郎", "age": 16},{"id": 2, "name": "二郎", "age": 20}]
async def update_users(users: List[User]):
    for new_user in users:
        user = (
            session.query(UserTable)
            .filter(UserTable.id == new_user.id)
            .first()
        )
        user.name = new_user.name
        user.age = new_user.age
        session.commit()
