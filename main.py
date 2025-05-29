#FastAPI 진입점
import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI
from monitor.monitor_second_check import monitor_attendance
from scheduler.scheduler import start_scheduler
from routers import bluetooth_api, second_check_api, attendance_api, statistics_api, today_lecture_api, login
from fastapi.middleware.cors import CORSMiddleware
from admin_router import attendance, summary, alerts
#from scheduler import monitor_attendance
#from scheduler import start_schedule



@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        start_scheduler()
        asyncio.create_task(monitor_attendance())
        print("✅ 스케줄러 및 감시 작업 시작됨")
        yield
    except Exception as e:
        print(f"❌ lifespan 내부 오류: {e}")
        yield
    
    
app = FastAPI(lifespan=lifespan)

# ✅ CORS 허용 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Android 앱에서 접속 가능하도록 전체 허용 (*). 운영 시엔 IP로 제한 권장
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def index():
    return "출석 알람 시스템 작동 중입니다!"





app.include_router(second_check_api.router)
app.include_router(bluetooth_api.router)
app.include_router(attendance_api.router)
app.include_router(statistics_api.router)
app.include_router(attendance.router)
app.include_router(summary.router)
app.include_router(alerts.router)
app.include_router(login.router)
