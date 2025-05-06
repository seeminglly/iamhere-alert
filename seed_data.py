# test_insert.py
from sqlalchemy.orm import Session
from db import SessionLocal
from models import Attendance
from datetime import datetime

session: Session = SessionLocal()

attendance = Attendance(
    user_id=13,
    lecture_id=5,
    method="Bluetooth",
    mac_address="AA:BB:CC:DD:EE:01",
    check_in=datetime.now(),
    status="2차출석완료"
)

session.add(attendance)
session.commit()
session.close()
print("✅ 출석 테스트 데이터 삽입 완료")
