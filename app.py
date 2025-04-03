from flask import Flask
from scheduler import start_scheduler
#from scheduler import check_attendance
import asyncio
from quart import Quart

#Flask 객체 인스턴스 생성
app = Quart(__name__)

@app.route('/')
def index():
    return "출석 알람 시스템 작동 중입니다!"

async def main():
    start_scheduler()  # AsyncIOScheduler 등록
    await app.run_task(debug=True)  # 비동기 서버 실행

if __name__ == "__main__":
    asyncio.run(main())