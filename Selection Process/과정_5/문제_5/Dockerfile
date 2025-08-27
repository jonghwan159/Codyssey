# Docker Hub의 Python 공식 이미지 사용
FROM python:3

# 작업 디렉토리 설정
WORKDIR /app

# 모든 파일 복사
COPY . .

# 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

# 컨테이너 포트 80 공개
EXPOSE 80

# gunicorn으로 앱 실행 (main.py에서 app 객체 사용 시)
CMD ["gunicorn", "main:app", "--bind", "0.0.0.0:80"]
