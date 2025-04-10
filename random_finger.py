# 학생 DB 참고해서 인원 수의 5%(소수점은 반올림)에게 알림
# 알림을 보낸 시점으로부터 5분 내로 서버에서 지문인식 완료 정보가 
# 넘어오지 않으면 결석
from datetime import datetime
import random

users = {
    f"student_{i+1}": {
        "student_id": f"2023{i+1:04}",
        "class_id": 100 if i < 10 else 101,  # 앞 10명은 100반, 뒤 10명은 101반
        "finger_check":False #지문인식 여부 default = false
    }
    for i in range(20)
}

#서버 -> 학생에게 지문인식 요청 알림 전송
def trigger_random_check(class_id, percentage = 5): #5%학생
     # 해당 class_id에 속한 학생들만 필터링
    candidates = [
        {"uuid": uuid, **info}
        for uuid, info in users.items()
        if info.get("class_id") == class_id
    ]

    total = len(candidates)
    if total == 0:
        print("[INFO] 해당 수업에 등록된 학생이 없습니다.")
        return
    count = max(1, total * percentage // 100) 
    # 무작위 추출
    selected = random.sample(candidates, count)

    # 결과 출력=> 실제로는 어플 알람/웹사이트 알람 메세지
    for student in selected:
        #print(f"[ALERT] {student['name']} (ID: {student['student_id']})에게 지문 알림 전송!")
        print(f"[ALERT] (ID: {student['student_id']})에게 지문 알림 전송!")
        after_finger_check(student)

#알림을 받은 학생들의 지문이 인식되었는지 확인하는 함수(라즈베리파이 서버-> DB 업데이트 후 확인인)
def after_finger_check(student):
    if student["finger_check"] == False:
        #학생DB의 출결을 결석으로 변경
        print("지문 인식 미완료로 결석 처리되었습니다.")
    else:
        print("지문인식 완료!")