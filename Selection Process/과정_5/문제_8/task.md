# ✅ DockerHub 이미지 다운로드 및 실행 과제 정리
## 1. DockerHub 로그인 (Access Token 사용)
```bash
docker login
# Username: <DockerHub ID 입력>
# Password: <Access Token 입력>
```
📌 Access Token은 DockerHub 웹사이트 > Account Settings > Security > New Access Token에서 생성할 수 있어요.

## 2. david:v1.0 이미지 다운로드 (Pull)
```bash
docker pull <DockerHub ID>/david:v1.0
# 예: docker pull jonghwan159/david:v1.0
```

## 3. 이미지 목록 확인
```bash
docker images
```
출력 결과에 david 이미지와 v1.0 태그가 보여야 해요.

## 4. 컨테이너 실행 (호스트: 80, 컨테이너: 80)
```bash
docker run -d -p 80:80 --name david-web <DockerHub ID>/david:v1.0
```
> -d 옵션: 백그라운드 실행
> --name: 컨테이너 이름 지정 (선택 사항)

## 5. 웹브라우저 확인 (가상머신에서 Firefox 실행)
---
### ✅ WSL2에서 Firefox 실행하는 방법
🔹 전제 조건
- Windows 11 사용 중

- wsl --version 명령어로 WSL이 최신인지 확인

- Ubuntu가 WSL2로 설정되어 있음

- wslg 기능 활성화됨 (Windows 11에 기본 탑재됨)

#### ✅ 1. Firefox 설치
```bash
sudo apt update
sudo apt install -y firefox
```
#### ✅ 2. Firefox 실행
```bash
firefox
```
- 이 명령어를 입력하면 Windows GUI 창에서 Firefox 브라우저가 실행됩니다.

- 주소창에 http://localhost 또는 http://127.0.0.1 입력하여 Docker 컨테이너가 잘 동작하는지 확인합니다.
---

- Ubuntu 가상머신에 설치된 Firefox 실행

- 주소창에 http://localhost 또는 http://127.0.0.1 입력

- Hello, DevOps! 같은 메시지가 보이면 성공

## 6. 컨테이너 목록 확인
```bash
docker ps -a
```
여기서 실행된 컨테이너의 CONTAINER ID 확인 가능

## 7. 컨테이너 내부 접속 (bash 실행)
```bash
docker exec -it david-web bash
# 또는 docker exec -it <CONTAINER ID> bash
```
- 내부에서 ls, cat 등으로 파일 확인 가능

## 8. 컨테이너 종료 및 삭제
```bash

docker stop david-web
docker rm david-web
```