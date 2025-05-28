from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from db import SessionLocal
from models import Enrollment, User
import random

from notify.pre_alert import send_second_alert
from notify.post_alert import send_result_alert

router = APIRouter()

@router.post("/attendance/second-check")
def trigger_second_check(lecture_id: int, percentage: int = 10):
    session: Session = SessionLocal()
    try:
        # 해당 수업 수강 학생 가져오기
        enrollments = session.query(Enrollment).filter_by(lecture_id=lecture_id).all()
        if not enrollments:
            raise HTTPException(status_code=404, detail="해당 수업의 수강생이 없습니다.")

        user_ids = [e.user_id for e in enrollments]
        users = session.query(User).filter(User.user_id.in_(user_ids)).all()

        # 몇 명 뽑을지 계산
        sample_count = max(1, round(len(users) * (percentage / 100)))
        selected = random.sample(users, sample_count)

        # 알림 전송 (예시: 콘솔에 출력)
        for user in selected:
            print(f"📢 [2차 지문 요청] {user.name}님에게 지문인식 요청 전송됨.")
            send_second_alert(user.name, lecture_id)

        return {"message": f"{sample_count}명의 학생에게 지문 요청 전송 완료."}

    finally:
        session.close()

@router.get("/attendance/second-check")
def trigger_fingerprint_check(name: str, lecture_title: str):
    session: Session = SessionLocal()
    try:
        print(f"📢 [2차 지문 요청] {name}님에게 지문인식 요청 전송됨.")
        send_second_alert(name, lecture_title)
        return {"message": f"{name} 학생에게 지문 요청 전송 완료."}

    finally:
        session.close()

@router.get("/attendance/second-result")
def trigger_fingerprint_result(name: str, result: bool):
    session: Session = SessionLocal()
    s = "성공함" if result else "실패함"
    try:
        print(f"📢 [2차 지문 출석 결과] {name}님의 지문인식이 {s}.")
        # ✅ FCM 알림 전송
        send_result_alert(name, result)

        return {"message": f"{name} 학생에게 지문 인식 결과 전송 완료."}

    finally:
        session.close()
