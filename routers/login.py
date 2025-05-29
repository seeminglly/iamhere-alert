from fastapi import APIRouter, HTTPException
from models import LoginRequest
from models import LoginResponse
from db import get_db_connection


from auth.createToken import CreateToken


router = APIRouter()# 로그인 API


@router.post("/login", response_model=LoginResponse)
async def login(request: LoginRequest):
    # 사용자 확인
    conn = get_db_connection()
    cursor = conn.cursor()

    sql = "SELECT * FROM users WHERE login_id = %s AND password = %s"
    cursor.execute(sql, (request.login_id, request.password))
    user = cursor.fetchone()

    if not user:
        conn.close()
        raise HTTPException(status_code=401, detail="잘못된 로그인 정보입니다.")
    conn.close()
    
    # 토큰 생성
    try:
        access_token = CreateToken(data={"sub": request.login_id})
        #Send_alarm(access_token) //학생인지 교수인지, userid를 보내야하나?
        return LoginResponse(access_token=access_token, token_type="bearer",user_name=user['name'], user_id=user['login_id'])#today_lectures
    except Exception as e:
        # 여기서 예외 로그 출력
        print(f"Login error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    


