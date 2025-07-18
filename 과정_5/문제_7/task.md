# ✅ 수행과제 명령어 실행 순서

## 0. WSL2 설정 및 Ubuntu 설치 및 실행
(이미 설치했다면 넘어가도 됩니다)

```powershell
# PowerShell (관리자 권한)
wsl --install
# 설치 완료 후 재부팅 → 자동으로 Ubuntu 설치됨
```

- 이후 Windows의 시작 메뉴에서 Ubuntu 검색 및 실행 후 터미널에서 아래 명령어 실행

## 1. Docker 최신 버전 설치 (Ubuntu)
```bash
sudo apt update
sudo apt install -y ca-certificates curl gnupg lsb-release
```
1. 디렉토리 생성:
```bash
sudo mkdir -p /etc/apt/keyrings
```
2. Docker GPG 키 다운로드 및 등록:
```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```

## 만약 안된다면 DNS 직접 고정하기
WSL2는 윈도우 DNS를 따라가는데 이게 종종 깨져요. 아래처럼 수동으로 설정해 주세요.

① 자동 생성 막기
```bash
sudo rm /etc/resolv.conf
sudo bash -c 'echo "nameserver 8.8.8.8" > /etc/resolv.conf'
sudo chattr +i /etc/resolv.conf  # 수정 방지
```
8.8.8.8은 구글 DNS예요. 1.1.1.1 (Cloudflare)도 가능.

## 이어서 진행
```bash
# 저장소 추가
echo \
  "deb [arch=$(dpkg --print-architecture) \
  signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# 설치
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
## 2. 현재 사용자에게 Docker 권한 부여
```bash
sudo usermod -aG docker $USER
# 이후 반영을 위해 재로그인
newgrp docker
```
## 3. hello-world 이미지 실행
```bash
docker run hello-world
```

## 4. Docker 이미지 목록 확인
```bash
docker images
```

## 5. 컨테이너 전체 목록 확인 및 삭제
```bash
docker ps -a

# hello-world 컨테이너가 있다면 ID 확인 후 정지 (예: abc123 컨테이너 ID)
docker stop abc123

# 컨테이너 삭제
docker rm abc123

```

## 6. hello-world 이미지 삭제
```bash
docker rmi hello-world
```

# 🏅 보너스 과제: 리눅스 컨테이너 실행 차이 & WSL2 필요 이유

## ✅ 리눅스 vs Windows/Mac에서 컨테이너 실행 차이

| 항목 | Linux (Ubuntu 등) | Windows/Mac |
|------|-------------------|--------------|
| 커널 구조 | 컨테이너가 호스트 리눅스 커널 직접 사용 | WSL2 (Linux 커널 VM) 또는 Hyper-V 사용 |
| 성능 | 네이티브 실행 (빠름) | 가상화 계층 필요 (약간 느릴 수 있음) |
| 복잡도 | 단순 설치 및 실행 | 추가 설정 (WSL2, Hyper-V 등) 필요 |
| 안정성 | 높은 호환성 및 성능 | 설정/버전 차이로 오류 발생 가능성 존재 |

---

## ✅ Windows에서 리눅스 컨테이너 실행에 WSL2가 필요한 이유

- **리눅스 컨테이너는 Linux 커널 의존**
- Windows에는 Linux 커널이 기본 탑재되어 있지 않음
- Docker Desktop은 WSL2를 통해 리눅스 커널 가상화
- WSL2는 고성능, 경량 가상화로 네이티브에 가까운 실행 환경 제공

**요약:** Windows에서 리눅스 커널 없이 리눅스 컨테이너 실행이 불가능하므로 WSL2가 필수임.