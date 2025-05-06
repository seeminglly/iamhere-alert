def send_post_attendance_alert(user_name: str):
    print(f"📢 [출석 완료] {user_name}님, 1차 출석이 성공적으로 완료되었습니다.")
def send_post_fail_alert(user_name: str):
    print(f"📢 [출석 실패] {user_name}님, 1차 출석이 실패하였습니다.")
def send_second_post_alert(user_name: str):
    print(f"📢 [출석 완료] {user_name}님, 2차 출석이 성공적으로 완료되었습니다.")
def send_second_fail_alert(user_name: str):
    print(f"📢 [출석 실패] {user_name}님, 2차 출석이 실패하였습니다.")