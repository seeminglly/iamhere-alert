@router.get("/attendance/calendar")
def get_calendar_data(user_id: int, db: Session = Depends(get_db)):
    records = db.query(Attendance).filter(
        Attendance.user_id == user_id
    ).all()

    return [
        {
            "date": r.check_in.date().isoformat(),
            "status": r.status  # 예: '1차출석완료', '1차출석실패', '2차출석실패'
        }
        for r in records
    ]

