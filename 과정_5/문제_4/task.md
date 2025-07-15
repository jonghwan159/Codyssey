# ✅ 최종 작업 디렉토리 구조 (Codyssey 기준)
```css
Codyssey/
├── app.py               ← Flask 앱 (main.py가 아니라 app.py 사용 시 기준 변경)
├── requirements.txt     ← flask, gunicorn, gTTS
├── Dockerfile
├── .dockerignore
├── .git/
├── venv/
├── 과정_1/
├── 과정_5/
├── 과정_6/
└── README.md
```
과정_1, 과정_5, 과정_6은 그대로 두고, 도커 관련 파일만 루트에 추가

# 📄 requirements.txt
```txt
flask
gunicorn
gTTS
```
# 📄 Dockerfile (Flask 객체가 app.py 안에 있다고 가정)
```Dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 80
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:80"]
```
🔁 만약 Flask 객체가 main.py 안에 있으면 CMD ["gunicorn", "main:app", ...]로 수정

# 📄 .dockerignore
```dockerignore
.git
.gitignore
.dockerignore
Dockerfile
venv
__pycache__
과정_1/
과정_5/
과정_6/
```
→ 도커 이미지 빌드 시 필요 없는 학습 폴더들 제외

# ✅ 빌드 & 실행 명령어 (Codyssey 폴더에서)
``` powershell
cd "C:\Users\whdgh\OneDrive\Desktop\Codyssey\Codyssey"

# 빌드
docker build -t codyssey-flask .

# 실행
docker run -it -p 8080:80 codyssey-flask
```
👉 그러면 브라우저에서 http://localhost:8080 으로 접속 가능

