# 라즈베리파이에서 5초 스캔이 끝난 후(scan_bluetooth_devices) 
# -> 비동기 방식으로 5초 대기 후에 자동으로 이 api호출

# routers/bluetooth_api.py
from fastapi import APIRouter
from monitor.check_bluetooth_attendance import process_bluetooth_attendance

router = APIRouter()

@router.post("/attendance/process-bluetooth")
def run_attendance_check():
    print(f"📢 [1차 출석] 1차 출석 여부 확인 중")
    process_bluetooth_attendance()
    return {"message": "1차 출석 확인 완료"}
