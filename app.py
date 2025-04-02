from flask import Flask
from scheduler import start_scheduler

app = Flask(__name__)

@app.route('/')
def index():
    return "출석 알람 시스템 작동 중입니다!"

if __name__ == '__main__':
    start_scheduler()
    app.run(debug=True)
