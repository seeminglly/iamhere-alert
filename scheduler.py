#from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta
import asyncio
from datetime import datetime

#name : 사용자 이름
#schedule_time[] : 사용자의 스케쥴 시작 시간(ex.09:00)

#하드코딩(학생+수업 스케쥴 데이터베이스)
users = [
    {
    "name":"강세민",
    "schedule_time":["23:40","23:41","23:42"]
    },
     {
    "name":"백재승",
    "schedule_time":["23:40","23:41","23:43"]
    },
     {
    "name":"홍길동동",
    "schedule_time":["23:40","23:41","23:44"]
    }
]


async def send_alert(name, time):
    now = datetime.now()
    print(f"🔔 {name}님! 출석 시작 10분 전입니다. ({time})")
    print("현재 시간 : ", now.time())
    await asyncio.sleep(0.01)

async def check_attendance(): #APScheduler가 실행하는 함수
    now = datetime.now().replace(second=0, microsecond=0)
    print(f"[{now.strftime('%H:%M')}] 출석 알림 점검 중...")
   


    tasks = [] # 비동기 작업 리스트

    for user in users:
        for time in user["schedule_time"]:
        # 문자열을 datetime으로 변환
            user_time = datetime.strptime(time, "%H:%M") #datetime객체로 변환
            # 오늘 날짜 + 출석 시간으로 통일
            att_time = now.replace(hour=user_time.hour, minute=user_time.minute, second=0)
            alarm_start = att_time - timedelta(minutes=10, seconds=10)
            alarm_end = att_time - timedelta(minutes=9, seconds=50)

            if alarm_start <= now <= alarm_end:
                # 알림을 비동기 task로 추가
                tasks.append(send_alert(user["name"], time))
     # 등록된 모든 알림 작업을 동시에 실행
    await asyncio.gather(*tasks)

        
#asyncio.run(check_attendance())
def start_scheduler():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(check_attendance, 'cron', second=0)
    scheduler.start()

