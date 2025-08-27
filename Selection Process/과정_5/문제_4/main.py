from flask import Flask

# Flask 애플리케이션 객체 생성
app = Flask(__name__)

# 라우팅 설정: "/" 경로로 접속 시 hello_world 함수 실행
@app.route("/")
def hello_world():
    return "Hello, DevOps!"

# 서버 실행
if __name__ == "__main__":
    # 호스트: 0.0.0.0, 포트: 80 설정
    app.run(host="0.0.0.0", port=80)
