from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta

users = [
    {"name":"김수정", "schedule_time":"09:00"},
    {"name":"수룡이", "schedule_time":"12:00"},
    {"name":"강세민", "schedule_time":"11:39"},
    {"name":"홍길동", "schedule_time":"11:42"},
]

def check_attendance():
    now = datetime.now()

    for user in users:
        # 문자열을 datetime으로 변환
        user_time = datetime.strptime(user["schedule_time"], "%H:%M")
        # 오늘 날짜 + 출석 시간으로 통일
        att_time = now.replace(hour=user_time.hour, minute=user_time.minute, second=0)
        
        # 출석 10분 전인지 확인
        if now >= att_time - timedelta(minutes=10) and now < att_time - timedelta(minutes=9):
            print(f"🔔 {user['name']}님! 출석 시간 10분 전입니다. ({user['schedule_time']})")


def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_attendance, 'interval', minutes=1)  # 매 1분마다 실행
    scheduler.start()
