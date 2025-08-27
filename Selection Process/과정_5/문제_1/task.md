# 1. Docker Desktop 설치
# https://www.docker.com/products/docker-desktop/ 에서 운영체제에 맞게 설치
# 설치 후, 아래 명령어로 설치 확인
docker --version

# 2. hello-world Docker 이미지 실행
sudo docker run hello-world

# 3. 이미지 목록 확인
sudo docker images

# 4. hello-world 이미지의 상세 정보 확인
sudo docker inspect hello-world

# 5. 컨테이너 전체 목록 및 상태 확인
sudo docker ps -a

# 6. 실행된 컨테이너의 상세 정보 확인 (컨테이너 ID는 실제 값으로 대체)
sudo docker inspect <컨테이너_ID>

# 예시: 가장 최근 생성된 컨테이너 확인 및 inspect
sudo docker ps -a -n 1
sudo docker inspect $(docker ps -a -n 1 -q)

# 7. hello-world 이미지의 히스토리 출력
sudo docker history hello-world

# 8. hello-world 컨테이너 및 이미지 삭제
# 컨테이너 삭제
sudo bash -c 'docker rm $(docker ps -a -q --filter ancestor=hello-world)'
# 이미지 삭제
sudo docker rmi hello-world