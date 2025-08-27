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

### 6) 토큰 PC에 저장(자동 로그인)
```bash
# Windows
git config --global credential.helper manager-core

# macOS
git config --global credential.helper osxkeychain

# Linux
git config --global credential.helper libsecret
```

## 문제 2. 함께 일하는 즐거움을 위해서 🤝
### 1) 원격 저장소 생성

- GitHub 웹 → 새 저장소(david) 생성 (Public)

### 2) 로컬 프로젝트(app.py) 디렉토리 이동
```bash
cd /path/to/project
```
### 3) Git 초기화 및 원격 추가
```bash
git init
git add .
git commit -m "init"

git remote add origin https://github.com/<YOUR_ID>/david.git
git remote -v   # 확인
```
### 4) main 브랜치 푸시
```bash
git branch -M main
git push -u origin main
```

### 5) add-image 브랜치 푸시
```bash
git checkout -b add-image
git add .
git commit -m "Add images"
git push -u origin add-image
```

### 6) 브랜치 확인
```bash
git branch -r
# 또는 GitHub 웹 → Branches 탭 확인
```


## 문제 3. 소스코드는 꼭 필요한 것만 🧹

### 1) .gitignore 추가
- 깃허브 사이트에서 addfile ->  .gitignore  
```bash
__pycache__
.venv
```
- 커밋 메세지 입력

### 2) 원격 저장소 내려받기
```
cd ~
git clone https://github.com/<YOUR_ID>/david.git david-clone
```
### 3) 원격에 올라간 불필요 폴더 삭제
```bash
git rm -r --cached __pycache__
git rm -r --cached .venv
git commit -m "Remove cached __pycache__ and .venv"
git push origin main
```

# 보너스 과제 🎁

## 문제 1: 인기 오픈소스 Fork 및 토큰 관리 보안

- Star 100개 이상 오픈소스 Fork
-> SeleniumBase

### 토큰 파일 삭제 이유

- 토큰은 비밀번호와 동일한 권한 → 평문 저장 시 유출 위험

- Git 커밋 등으로 유출 가능성 있음 → 임시 확인 후 삭제

## 문제 2: 저장소 복제
```bash
git clone https://github.com/jonghwan159/david.git
```

## 문제 3: 파이썬 프로젝트에서 .gitignore 사용 이유

- __pycache__: Python이 바이트코드(.pyc)를 저장하는 캐시

- .venv: 가상환경 디렉토리 (환경 종속적, 공유 불필요)

- GitHub Python 템플릿에 포함되는 항목: __pycache__/, .venv/, *.pyc, .mypy_cache/, .pytest_cache/, build/, dist/ 등

- Flask 프로젝트 권장 .gitignore 추가 항목

```bash
instance/
.env
.flaskenv
*.db
*.sqlite3
*.log
.pytest_cache/
.coverage
htmlcov/
.vscode/
.idea/
```
