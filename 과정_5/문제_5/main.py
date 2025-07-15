from flask import Flask

# Flask 애플리케이션 객체 생성
app = Flask(__name__)

# 라우팅 설정: "/" 경로로 접속 시 실행될 함수
@app.route("/")
def hello_world():
    return "Hello, DevOps!"

# 직접 실행 시 Flask 내장 서버가 실행되지만
# Docker에서는 gunicorn이 실행함
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
