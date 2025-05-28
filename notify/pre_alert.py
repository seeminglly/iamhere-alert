from datetime import datetime
from notify.utils import get_user_token
from notify.fcm import send_fcm_v1  # 경로는 실제 구조에 맞게 조정하세요

def send_pre_attendance_alert(name: str, lecture_title: str):
    now = datetime.now().strftime("%H:%M:%S")
    message = f"🔔  {name}님! 곧 [{lecture_title}] 수업이 시작됩니다. 출석 준비해주세요! ({now})"
    print(message)

    token = get_user_token(name)
    if token:
        send_fcm_v1(token, "출석 알림", f"[{lecture_title}] 수업이 곧 시작됩니다. 출석해주세요!")

def send_second_alert(name: str, lecture_title: str):
    now = datetime.now().strftime("%H:%M:%S")
    message = f"🔔  {name}님! [{lecture_title}] 2차 지문인증 출석을 진행해주세요! ({now})"
    print(message)

    token = get_user_token(name)
    if token:
        send_fcm_v1(token, "2차 출석 요청", f"[{lecture_title}] 수업 2차 지문 인증을 해주세요!")

