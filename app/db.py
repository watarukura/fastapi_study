# DBへの接続設定
import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


# 接続したいDBの基本情報を設定
user = os.getenv("USER")
password = os.getenv("PASSWORD")
host = "db"
database = os.getenv("DB")

DATABASE = (
    f"mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8mb4"
)

# DBとの接続
ENGINE = create_engine(DATABASE, encoding="utf-8", echo=True)

# Sessionの作成
session = scoped_session(
    # ORM実行時の設定。自動コミットするか、自動反映するか
    sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)
)

# modelで使用する
Base = declarative_base()
# DB接続用のセッションクラス、インスタンスが作成されると接続する
Base.query = session.query_property()
