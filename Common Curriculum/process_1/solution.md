# GitHub 과제 수행 과정 정리

## 문제 1. 커피를 좋아하는 동료들을 위해서 ☕️

### 1) GitHub 시작하기(빠른시작) 확인
- GitHub 공식 문서(https://docs.github.com/ko/get-started)

### 2) GitHub 가입 및 로그인
- 계정 생성 후 로그인

### 3) 유료·무료 요금제 차이
- **무료(Free)**: 퍼블릭/프라이빗 리포 무제한, 기본 Actions 제한
- **유료(Pro)**: Actions/스토리지 확대, 고급 코드 리뷰 등

### 4) Personal Access Token(PAT) 생성
- `Settings → Developer settings → Personal access tokens`
- repo 권한 선택 후 발급

### 5) 토큰 텍스트 저장 후 삭제
```bash
echo "ghp_xxxYOUR_TOKEN_xxx" > ~/github_pat.txt
cat ~/github_pat.txt   # 확인
rm ~/github_pat.txt    # 인증 후 삭제
```