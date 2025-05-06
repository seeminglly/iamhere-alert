from datetime import datetime


def send_pre_attendance_alert(name: str, lecture_title: str):
    now = datetime.now().strftime("%H:%M:%S")
    print(f"🔔 {name}님! 곧 [{lecture_title}] 수업이 시작됩니다. 출석 준비해주세요! ({now})")
def send_second_alert(name: str, lecture_title: str):
    now = datetime.now().strftime("%H:%M:%S")
    print(f"🔔 {name}님! [{lecture_title}] 2차 지문인증 출석을 진행해주세요! ({now})")