# 예시: schemas.py 또는 routers/login_router.py 안에

from pydantic import BaseModel
class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    user_id: int
    user_name: str
    role: str
    student_number: Optional[str] = None  # ✅ 학번 추가 (교수는 None일 수 있음)

