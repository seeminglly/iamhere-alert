from sqlalchemy import Integer, Column, BigInteger, String, Enum, Time, Date, ForeignKey, Text, TIMESTAMP
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

# ✅ users 테이블
class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True)
    name = Column(String(100))
    role = Column(Enum("학생", "교수"))
    password = Column(String(100))
    login_id = Column(String(100))
    student_id = Column(String(50))
    major = Column(String(100))
    fcm_token = Column(Text)  # ✅ FCM 토큰 필드 추가

# ✅ lectures 테이블
class Lecture(Base):
    __tablename__ = "lectures"

    lecture_id = Column(BigInteger, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    day = Column(Enum('월','화','수','목','금'), nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)

# ✅ fingerprints 테이블
class Fingerprint(Base):
    __tablename__ = "fingerprints"

    user_id = Column(BigInteger, ForeignKey("users.user_id", ondelete="CASCADE"), primary_key=True)
    fingerprint_template = Column(Text, nullable=False)

# ✅ bluetooth_devices 테이블
class BluetoothDevice(Base):
    __tablename__ = "bluetooth_devices"

    device_id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False)
    mac_address = Column(String(17), unique=True, nullable=False)
    device_name = Column(String(255))
    registered_at = Column(TIMESTAMP)

# ✅ enrollments 테이블
class Enrollment(Base):
    __tablename__ = "enrollments"

    enrollment_id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("users.user_id"))
    lecture_id = Column(BigInteger, ForeignKey("lectures.lecture_id", ondelete="CASCADE"))

# ✅ attendances 테이블
class Attendance(Base):
    __tablename__ = "attendances"

    attendance_id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("users.user_id", ondelete="SET NULL"))
    lecture_id = Column(BigInteger, ForeignKey("lectures.lecture_id", ondelete="SET NULL"))
    method = Column(Enum('Bluetooth', 'Fingerprint', 'Both'), nullable=False)
    mac_address = Column(String(17), ForeignKey("bluetooth_devices.mac_address", ondelete="SET NULL"))
    check_in = Column(TIMESTAMP)
    status = Column(Enum('1차출석완료', '1차출석실패', '2차출석완료', '2차출석실패', '2차출석제외'), nullable=False)
