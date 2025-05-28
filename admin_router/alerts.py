# admin_router/alerts.py
from fastapi import APIRouter
from datetime import datetime

router = APIRouter(prefix="/admin", tags=["admin"])

@router.get("/alerts")
def get_alerts():
    return [
        {"message": "지문 인식 실패 - 홍길동", "time": "09:01"},
        {"message": "등록되지 않은 사용자 - 김철수", "time": "09:03"}
    ]

