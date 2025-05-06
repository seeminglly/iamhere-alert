# 조건: 블루투스 스캔 5초 후 → 한 번만 출석 상태 확인
# 처리 방식: 단발성 함수 호출

from datetime import datetime, timedelta
from db import SessionLocal
from models import Attendance
from notify.post_alert import send_post_attendance_alert, send_post_fail_alert


def process_bluetooth_attendance():
    # 블루투스 스캔 완료 후 한 번만 실행
    session = SessionLocal()
    try:
        now = datetime.now()
        five_seconds_ago = now - timedelta(seconds=5)

        records = session.query(Attendance).filter(
            Attendance.check_in >= five_seconds_ago,
            Attendance.status.in_(["1차출석완료", "1차출석실패"])
        ).all()

        for record in records:
            if record.status == "1차출석완료":
                send_post_attendance_alert(record.user_id)
            elif record.status == "1차출석실패":
                send_post_fail_alert(record.user_id)

    finally:
        session.close()
