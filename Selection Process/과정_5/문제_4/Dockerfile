# 베이스 이미지 (DockerHub Official Image)
FROM python:3.10-slim

# 작업 디렉토리 설정
WORKDIR /app

# 로컬 파일 전체 복사
COPY . .

# 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

# 포트 노출
EXPOSE 80

# 컨테이너 실행 명령
CMD ["gunicorn", "main:app", "--bind", "0.0.0.0:80"]
