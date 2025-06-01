from fastapi import APIRouter, HTTPException
from models import LoginRequest, LoginResponse
from db import get_db_connection
from auth.createToken import CreateToken

router = APIRouter()

@router.post("/login", response_model=LoginResponse)
async def login(request: LoginRequest):
    # DB 연결 및 사용자 조회
    conn = get_db_connection()
    cursor = conn.cursor()

    sql = "SELECT * FROM users WHERE login_id = %s AND password = %s"
    cursor.execute(sql, (request.login_id, request.password))
    user = cursor.fetchone()
    conn.close()

    if not user:
        raise HTTPException(status_code=401, detail="잘못된 로그인 정보입니다.")

    # 토큰 생성
    try:
        access_token = CreateToken(data={"sub": request.login_id})

        return LoginResponse(
            access_token=access_token,
            token_type="bearer",
            user_id=str(user["user_id"]),
            user_name=user["name"],  # 이름
            student_number=user.get("student_number"),  # ✅ 학번
            role=user.get("role")  # 예: 학생, 교수 등
        )

    except Exception as e:
        print(f"Login error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

