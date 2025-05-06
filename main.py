#FastAPI 진입점
import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI
from monitor.monitor_second_check import monitor_attendance
from scheduler.scheduler import start_scheduler
from routers import bluetooth_api, second_check_api
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

@app.get('/')
async def index():
    return "출석 알람 시스템 작동 중입니다!"





app.include_router(second_check_api.router)
app.include_router(bluetooth_api.router)
