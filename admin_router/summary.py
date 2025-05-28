# admin_router/summary.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from models import Attendance
from sqlalchemy import func

router = APIRouter(prefix="/admin", tags=["admin"])

@router.get("/summary")
def get_summary(db: Session = Depends(get_db)):
    total = db.query(Attendance.user_id).distinct().count()
    attended = db.query(Attendance).filter(Attendance.status.in_(["1차출석완료", "2차출석완료"])).count()
    late = db.query(Attendance).filter(Attendance.status == "1차출석실패").count()
    absent = db.query(Attendance).filter(Attendance.status.in_(["2차출석실패", "2차출석제외"])).count()

    return {
        "total": total,
        "attended": attended,
        "late": late,
        "absent": absent,
        "lecture_date": "2025.05.03",  # 필요 시 lecture 테이블과 조인
        "lecture_info": "캡스톤 디자인 (수) 09:00-12:00"
    }

