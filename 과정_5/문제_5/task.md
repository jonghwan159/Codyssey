# ✅ 1. Dockerfile로 이미지 빌드 (david:v1.0)
```bash
docker build -t david:v1.0 .
```
- -t: 이미지 이름과 태그 지정 (이름: david, 태그: v1.0)

- .: 현재 디렉토리의 Dockerfile을 기준으로 빌드

# ✅ 2. david:v1.0 이미지 실행 (호스트:80 ↔ 컨테이너:80)
```bash

docker run -it -p 80:80 --name david-container david:v1.0
```
- -p 80:80: 호스트 80번 포트를 컨테이너 80번 포트에 연결

- --name david-container: 컨테이너 이름 지정

- 웹브라우저에서 http://localhost 접속 시 Flask 앱 확인 가능

# ✅ 3. 이미지 목록 확인
```bash
docker images
```
> david라는 이름과 v1.0 태그 확인

# ✅ 4. 실행 중인 컨테이너 ID 확인
```bash
docker ps
```
# ✅ 5. 컨테이너 내부 bash 진입 후 확인
```bash
docker exec -it david-container bash
```
## ✅ 내부에서 확인할 내용:
- Dockerfile 파일이 복사되었는지 (ls 명령어로 확인)

- .dockerignore에 명시된 항목들이 복사되지 않았는지 확인

예시:

```bash
ls -a
cat Dockerfile          # 존재하면 실패 (dockerignore 대상이어야 함)
cat .dockerignore       # 존재하면 실패
cat .gitignore          # 존재하면 실패
ls .git                 # 없어야 정상
```

# ✅ 6. 컨테이너 종료 및 삭제
```bash
docker stop david-container
docker rm david-container
```

# ✅ 7. 변경사항 Git 커밋 및 원격 저장소로 push
```bash
git add .
git commit -m "과정5 문제4: david:v1.0 이미지 빌드 및 테스트 완료"
git push origin main
```
# 🏅 보너스 과제: 리눅스 컨테이너 vs 윈도우 컨테이너 차이 (요약문서 예시)

## 리눅스 컨테이너 vs 윈도우 컨테이너 차이

### 1. 커널 공유 구조
- 리눅스 컨테이너: 호스트 OS의 Linux 커널을 공유
- 윈도우 컨테이너: Windows 커널 또는 Hyper-V 기반으로 실행

### 2. 실행 환경
- 리눅스 컨테이너는 Linux 기반 앱 실행에 적합
- 윈도우 컨테이너는 .NET Framework 등 Windows 앱 실행에 적합

### 3. 호환성
- Docker Desktop에서는 한 번에 하나의 컨테이너 모드만 사용 가능 (리눅스 or 윈도우)
- 기본값은 리눅스 컨테이너

### 4. 이미지 크기
- 윈도우 컨테이너 이미지는 크기가 큼 (수 GB 이상)
- 리눅스 컨테이너는 경량화되어 빠름

### 5. 성능
- 일반적으로 리눅스 컨테이너가 더 빠르고 자원 효율적