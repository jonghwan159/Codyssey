# ✅ Ubuntu 컨테이너 실습: Docker 명령어 모음
```bash
# 1. Docker Hub에서 ubuntu 이미지 검색
sudo docker search ubuntu

# 2. (웹브라우저에서) Docker Hub 접속 → https://hub.docker.com/_/ubuntu
# - Overview 탭에서 'Docker Official Image' 뱃지 확인
# - Tags 탭에서 '20.04' 검색 → 사용 예시와 Digest 확인 가능

# 3. ubuntu:20.04 이미지 다운로드
sudo docker pull ubuntu:20.04

# 4. 이미지 상세 정보 확인
sudo docker inspect ubuntu:20.04

# 5. 이미지 히스토리 확인
sudo docker history ubuntu:20.04
```
# ✅ Ubuntu 컨테이너 생성 및 파일 테스트
```bash
# 6. ubuntu:20.04 이미지로 bash 쉘 컨테이너 실행 (컨테이너 이름 미지정)
sudo docker run -it ubuntu:20.04 bash

# 7. 컨테이너 내부에서 파일 생성 (예: /tmp/hello.txt)
touch /tmp/hello.txt
exit
```
❗ 주의: 컨테이너를 exit하면 자동 삭제되므로, 다음 명령어로 컨테이너를 삭제하지 않고 종료하거나 이름을 지정해서 재사용할 수 있도록 하자.
```bash
# 6-2. 이름을 지정하여 실행
sudo docker run -it --name my-ubuntu-test ubuntu:20.04 bash

# 컨테이너 내부에서 파일 생성
touch /tmp/testfile.txt
exit

# 8. 파일 존재 여부 확인: 컨테이너 재실행
sudo docker start -ai my-ubuntu-test

# 파일 확인
ls /tmp
exit

# 9. 컨테이너 삭제
sudo docker rm my-ubuntu-test
```
# 🏅 보너스 과제: 컨테이너 이름 지정 시와 미지정 시 차이
```bash
# 보너스 과제: 컨테이너 이름 지정의 차이

## 1. 이름 미지정 시
- Docker는 자동으로 무작위 컨테이너 이름을 생성함 (예: `crazy_wilson`)
- 실행할 때마다 새로운 컨테이너가 생성되며 이전 컨테이너와 별개임
- 파일이나 상태가 유지되지 않음 (기본적으로 ephemeral)

## 2. 이름 지정 시
- 컨테이너 이름으로 식별 가능 (예: `--name my-ubuntu-test`)
- 정지 후에도 같은 컨테이너를 `start` 또는 `exec`로 재사용 가능
- 내부에 생성된 파일, 환경변수 등 상태가 유지됨

## 3. 예시 명령어 비교

### 이름 미지정

sudo docker run -it ubuntu bash

- 종료하면 컨테이너도 같이 종료되고, 다시 실행 시 새로운 컨테이너 생성

### 이름 지정

sudo docker run -it --name my-ubuntu ubuntu bash
sudo docker start -ai my-ubuntu

- 종료 후 다시 실행하면 이전 상태 그대로 사용 가능
```