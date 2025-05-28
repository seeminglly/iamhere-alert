from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from models import Attendance
from datetime import date
from pydantic import BaseModel
from typing import List

router = APIRouter()

@router.post("/attendance/first-check")
def first_attendance_check(user_id: int, db: Session = Depends(get_db)):
    # 여기선 단순히 출석 성공으로 가정
    from notify.post_alert import send_post_attendance_alert

    user = db.query(User).filter(User.user_id == user_id).first()
    if user:
        send_post_attendance_alert(user.name)
        return {"message": f"{user.name}님 출석 완료"}
    return {"error": "사용자를 찾을 수 없습니다."}

class CalendarRecord(BaseModel):
    date: date
    status: str

@router.get("/attendance/today")
def get_today_attendance(user_id: int, db: Session = Depends(get_db)):
    today = date.today()
    records = db.query(Attendance).filter(
        Attendance.user_id == user_id,
        Attendance.check_in >= today
    ).all()

    return [
        {
            "lecture_id": r.lecture_id,
            "status": r.status,
            "check_in": r.check_in.strftime("%H:%M")
        }
        for r in records
    ]

@router.get("/attendance/calendar", response_model=List[CalendarRecord])
def get_attendance_calendar(user_id: int, db: Session = Depends(get_db)):
    results = db.query(Attendance).filter(
        Attendance.user_id == user_id
    ).all()

    return [
        CalendarRecord(date=r.check_in.date(), status=r.status)
        for r in results
    ]

@router.get("/attendance/today-lecture")
def get_today_lecture(user_id: int, db: Session = Depends(get_db)):
    today = date.today()
    attendance = db.query(Attendance).filter(
        Attendance.user_id == user_id,
        Attendance.check_in >= today
    ).first()

    if not attendance:
        return {"title": "오늘은 수업 없음", "day": "", "time": ""}

    lecture = db.query(Lecture).filter(Lecture.lecture_id == attendance.lecture_id).first()
    return {
        "title": lecture.title,
        "day": lecture.day,
        "time": f"{lecture.start_time.strftime('%H:%M')} - {lecture.end_time.strftime('%H:%M')}"
    }

