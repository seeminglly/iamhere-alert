
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from sqlalchemy.orm import Session
from db import SessionLocal
from models import Enrollment, Lecture, User
from notify.pre_alert import send_pre_attendance_alert
from datetime import datetime, timedelta

scheduler = AsyncIOScheduler()

weekday_map = {
    "월": "mon", "화": "tue", "수": "wed", "목": "thu", "금": "fri", "토": "sat", "일": "sun"
}

def start_scheduler():
    print("✅ 스케줄러 시작됨")
    session: Session = SessionLocal()

    try:
        enrollments = session.query(Enrollment).all() 
        for enroll in enrollments:
            #DB에서 강의, 학생 정보 조회
            lecture = session.query(Lecture).filter(Lecture.lecture_id == enroll.lecture_id).first()
            student = session.query(User).filter(User.user_id == enroll.user_id).first()

            if not student or not lecture:
                    continue

            # 🔹 강의 요일 및 시간 정보로 스케줄 계산
            day = weekday_map.get(lecture.day)
            start_time = lecture.start_time
            pre_time = (datetime.combine(datetime.today(), start_time) - timedelta(minutes=10)).time()

            # 🔹 알림 예약
            scheduler.add_job(
                lambda s=student, l=lecture: send_pre_attendance_alert(s.name, l.title),
                    CronTrigger(
                        day_of_week=day,
                        hour=pre_time.hour,
                        minute=pre_time.minute
                    ),
                    id=f"pre_alert_{student.user_id}_{lecture.lecture_id}",  # 중복 방지를 위한 고유 ID
                    replace_existing=True
                )


            print(f"📌 [{lecture.title}] - {student.name} 수업 알림 예약됨 → {day} {pre_time}")
    finally:
        session.close()

    scheduler.start()
