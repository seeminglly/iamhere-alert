# init_db.py
from models import Base
from db import engine  # SQLAlchemy create_engine(...) 반환

def init_db():
    print("🛠️ DB 테이블을 생성합니다...")
    Base.metadata.create_all(bind=engine)
    print("✅ DB 테이블 생성 완료!")

if __name__ == "__main__":
    init_db()
