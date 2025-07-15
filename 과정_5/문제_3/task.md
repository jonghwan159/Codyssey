# ✅ Python 개발 환경 Docker 실습
1. python:3 이미지 다운로드
```bash
docker pull python:3
```
2. 컨테이너 실행 (bash 쉘 + 포트 80 연결 + 이름 지정)
```bash
docker run -it --name python-dev -p 80:80 python:3 bash
```
이 상태에서 bash로 진입됨.

3. (새 터미널 창에서) 현재 작업 디렉토리를 컨테이너로 복사
예: ~/workspace/myapp → /app에 복사

```bash
docker cp "C:\Users\whdgh\OneDrive\Desktop\Codyssey\Codyssey" python-dev:/app

```

4. 컨테이너 내부에서 필요한 패키지 설치

```bash
# 컨테이너 내부 bash
cd /app
pip install flask
pip intstall gtts
```
5. app.py 실행
```bash
python app.py
```
주의 :  처음 실행했을때 port랑 일치해야함
문제 2번의 app.py 실행해서 하면 될거임

``` python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Docker Python container!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
```

6. 웹브라우저에서 확인
접속 주소: http://localhost
→ 위 메시지가 뜨면 성공!

7. 컨테이너에서 이미지 저장
```bash
# 현재 컨테이너로부터 이미지 저장
docker commit python-dev python_david
```
8. 컨테이너 종료 및 삭제
```bash
docker stop python-dev
docker rm python-dev
```
9. 기존 python:3 이미지로 새 컨테이너 실행 → 파일 없음
```bash
docker run -it python:3 bash
ls /app  # 없음
exit
```
10. python_david 이미지로 새 컨테이너 실행 → 파일 있음
```bash
docker run -it python_david bash
ls /app  # 복사된 파일 확인됨
```
11. 모든 관련 컨테이너 종료 및 삭제
```bash
# 실행 중인 컨테이너 정지
# 중지
docker ps -a --filter ancestor=python:3 -q | ForEach-Object { docker stop $_ }

# 삭제
docker ps -a --filter ancestor=python:3 -q | ForEach-Object { docker rm $_ }

# 원하면 이미지도 삭제 가능
# sudo docker rmi python:3
```

# 🏅 보너스 과제: 호스트 포트와 컨테이너 포트의 차이

## 1. 컨테이너 포트란?
- 컨테이너 내부에서 서비스가 열리는 포트
- 예: `Flask` 앱이 컨테이너 내에서 `0.0.0.0:80`에 바인딩

## 2. 호스트 포트란?
- 호스트(PC)가 외부로 노출하는 포트
- 컨테이너 외부에서 접속하려면 이 포트를 통해 들어옴

## 3. 포트 매핑 예시
```bash
docker run -p 8080:80 ...
```
호스트의 8080포트 → 컨테이너의 80포트로 포워딩됨

즉, 외부 사용자가 localhost:8080으로 접속하면 실제 컨테이너의 80번 포트가 호출됨

4. 정리
항목	호스트 포트	컨테이너 포트
정의	PC에서 열리는 포트	컨테이너 내부에서 사용되는 포트
목적	외부와의 통신용	내부 서비스 실행용
명령어 예시	-p 8080:80	(Flask 앱이 port=80으로 바인딩됨)
