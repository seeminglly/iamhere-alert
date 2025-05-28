from sqlalchemy.orm import Session
from db import SessionLocal
from models import User

def get_user_token(name: str) -> str | None:
    session: Session = SessionLocal()
    try:
        user = session.query(User).filter(User.name == name).first()
        if user and user.fcm_token:
            return user.fcm_token
        return None
    finally:
        session.close()

