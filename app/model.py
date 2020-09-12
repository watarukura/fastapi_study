from pydantic import BaseModel
from pynamodb.attributes import NumberAttribute, UnicodeAttribute
from pynamodb.models import Model
from sqlalchemy import Column, Integer, String

from app.db import ENGINE, Base


class UserDdb(Model):
    class Meta:
        table_name = "user"
        region = "ap-northeast-1"
        host = "http://host.docker.internal:18000"

    id = NumberAttribute(hash_key=True)
    name = UnicodeAttribute(null=False)
    age = NumberAttribute(null=True)


# userテーブルのモデルUserTableを定義
class UserTable(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    age = Column(Integer)


# POSTやPUTのとき受け取るRequest Bodyのモデルを定義
class User(BaseModel):
    id: int
    name: str
    age: int


def main():
    # テーブルが存在しなければ、テーブルを作成
    Base.metadata.create_all(bind=ENGINE)
    if not UserDdb.exists():
        UserDdb.create_table(read_capacity_units=1, write_capacity_units=1)


if __name__ == "__main__":
    main()
