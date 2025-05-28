from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# ✅ 출결 응답 모델 (GET /admin/attendances)
class AttendanceResponse(BaseModel):
    attendance_id: int
    name: str
    student_id: Optional[str]  # student_id가 NULL일 수 있으므로 Optional 처리
    status: str
    check_in: datetime

    model_config = {
        "from_attributes": True  # Pydantic v2에서 orm_mode=True의 대체
    }

# ✅ 출결 수정 요청 모델 (PUT /admin/attendance/{id})
class UpdateAttendance(BaseModel):
    status: str  # 예: '1차출석완료', '2차출석실패', '2차출석제외'

