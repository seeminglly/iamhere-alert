#FastAPI 진입점
import asyncio
from fastapi import FastAPI
from random_finger import trigger_random_check
from scheduler import start_scheduler

app = FastAPI()


@app.get('/')
async def index():
    return "출석 알람 시스템 작동 중입니다!"

@app.get("/random_finger")
async def random_finger():
    trigger_random_check(100) #class_id=100인 사람에게 알림 -> 동적으로 id받도록 수정
    return {"message": "지문 알림 테스트 중입니다!"}

start_scheduler()