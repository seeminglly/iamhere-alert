from .fcm import send_fcm_v1
from .utils import get_user_token

def send_post_attendance_alert(user_name: str):
    print(f"📢   [출석 완료] {user_name}님, 1차 출석이 성공적으로 완료되었습니다.")
    token = get_user_token(user_name)
    print(f"🧪  FCM 토큰: {token}")
    if token:
        send_fcm_v1(token, "출석 완료", f"{user_name}님, 1차 출석이 성공적으로 완료되었습니다.")

def send_post_fail_alert(user_name: str):
    print(f"📢   [출석 실패] {user_name}님, 1차 출석이 실패하였습니다.")
    token = get_user_token(user_name)
    print(f"🧪  FCM 토큰: {token}")
    if token:
        send_fcm_v1(token, "출석 실패", f"{user_name}님, 1차 출석이 실패하였습니다.")

def send_second_post_alert(user_name: str):
    print(f"📢  [출석 완료] {user_name}님, 2차 출석이 성공적으로 완료되었습니다.")
    token = get_user_token(user_name)
    if token:
        send_fcm_v1(token, "2차 출석 완료", f"{user_name}님, 2차 출석이 완료되었습니다.")

def send_second_fail_alert(user_name: str):
    print(f"📢  [출석 실패] {user_name}님, 2차 출석이 실패하였습니다.")
    token = get_user_token(user_name)
    if token:
        send_fcm_v1(token, "2차 출석 실패", f"{user_name}님, 2차 출석이 실패하였습니다.")

def send_result_alert(name: str, result: bool):
    token = get_user_token(name)
    if not token:
        print(f"❗  {name}의 FCM 토큰을 찾을 수 없습니다.")
        return

    title = "2차 지문 인증 결과"
    body = f"{name}님의 지문 인증이 {'성공' if result else '실패'}했습니다."

    send_fcm_v1(token, title, body)

