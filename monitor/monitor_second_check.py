# monitor.py (DB 감시 루프)from sqlalchemy.orm import Session
# 조건: 알람 전송된 이후 10분간 주기적으로 출석 상태 감시
# 처리 방식: 비동기 루프로 상태 변화 감시
from db import SessionLocal
from models import Attendance
from datetime import datetime, timedelta
import asyncio

from notify.post_alert import send_second_post_alert, send_second_fail_alert

# 이미 알림 보낸 출석 기록 ID 저장용 set
notified_attendance_ids = set()

async def monitor_attendance():
    print("⏱️ 2차 출석 감시 시작")

    while True:
        session : Session = SessionLocal()

        try: #2차 출석 감시
            now = datetime.now()
            one_minutes_ago = now - timedelta(minutes=1)

            records = session.query(Attendance).filter(
                Attendance.check_in >= one_minutes_ago,
                Attendance.status.in_(["2차출석완료","2차출석실패"])
            ).all()

            for record in records:
                if record.attendance_id not in notified_attendance_ids:
                    if record.status == "2차출석완료":
                        send_second_post_alert(record.user_id)
                    elif record.status == "2차출석실패":
                        send_second_fail_alert
                notified_attendance_ids.add(record.attendance_id)
        except Exception as e:
            print(f"❗ 감시 중 오류: {e}")
        finally:
            session.close()

        await asyncio.sleep(1)  # 1초마다 감시

# 10분동안 1초마다 감시하도록 변경
# 지금은 서버 실행하자마자 쓸데없이 2차 출석 감시가 시작되는데 교수님이 2차 출석 버튼을 누르면 감시 시작되도록 변경(api호출?)