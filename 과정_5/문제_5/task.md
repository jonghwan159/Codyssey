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
git commit -m "feat/과정_5/문제_5"
git push origin main
```
# 🏅 보너스 과제: 리눅스 컨테이너 vs 윈도우 컨테이너 차이

| 항목           | 리눅스 컨테이너                                      | 윈도우 컨테이너                                       |
|----------------|-------------------------------------------------------|--------------------------------------------------------|
| 커널 구조      | 호스트의 Linux 커널을 공유                            | Windows 커널 또는 Hyper-V 기반으로 실행               |
| 실행 환경      | Linux 기반 앱에 적합 (Flask, Node.js 등)             | .NET Framework, IIS 등 Windows 앱 실행에 적합         |
| 호환성         | Docker Desktop 기본 설정 (한 번에 하나만 사용 가능) | "Switch to Windows containers"로 전환 가능            |
| 이미지 크기    | 작고 경량화되어 빠름                                 | 이미지가 크고 무거움 (수 GB 이상)                    |
| 성능           | 빠르고 자원 효율적                                   | Hyper-V 사용 시 느릴 수 있음                          |
