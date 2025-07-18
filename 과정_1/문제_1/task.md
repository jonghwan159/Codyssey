# ✅ 1. 윈도우 터미널 설치 (Windows Terminal)
PowerShell에서 아래 명령 실행:
```powershell
winget install --id Microsoft.WindowsTerminal -e
```
> winget이 없으면 최신 Windows로 업데이트 필요

# ✅ 2. Python 설치 (3.8 이상)
```powershell
Invoke-WebRequest -Uri "https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe" -OutFile "python-installer.exe"
Start-Process -FilePath ".\python-installer.exe" -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1 Include_test=0" -Wait
```
> 위 명령은 환경 변수(Path) 자동 등록까지 해줌

# ✅ 3. Python, pip 경로 확인
```powershell
python --version
pip --version
```
정상 출력되면 환경변수 등록 완료된 것임.

# ✅ 4. Flask 설치
```powershell
pip install flask
```
설치 확인:

```powershell
pip show flask
```

# ✅ 5. Python 실행 후 Hello 출력
```powershell
python
>>> print("Hello")
>>> exit()
```

# ✅ 6. 함수 작성 (my_solution.py)
PowerShell에서 아래로 파일 생성:
``` powershell
echo "def hello():`n    return 'Hello'" > my_solution.py
```

확인:

```powershell
type my_solution.py
```

# ✅ 7. Visual Studio Code 설치
```powershell
winget install --id Microsoft.VisualStudioCode -e
```

# ✅ 8. VS Code 실행 & 확장 설치
VS Code 열기
```powershell
code
```

확장 설치 (VS Code 안에서 입력)
1. Ctrl+Shift+X 누르기 (확장 탭 열기)

2. 검색창에 Material Icon Theme 입력 후 설치

3. Ctrl + Shift + P 누르기 → Command Palette 열기

4. "Icon Theme" 입력

5. Material Icons: Activate Icon Theme 클릭



# ✅ 보너스 과제: Markdown 작성

# Python의 대표 웹 프레임워크 3가지

## 1. Django
**특징**: 배터리가 포함된(Full-Stack) 프레임워크  
**장점**:
- ORM 내장
- 관리자 페이지 자동 생성
- 인증, 세션, CSRF 보안 등 기본 내장
- 프로젝트 구조가 명확하고 강력한 기능 제공

**적합한 경우**:  
빠르게 전체 웹 서비스를 만들고 싶은 경우, 대규모 서비스에 적합

---

## 2. Flask
**특징**: 마이크로 웹 프레임워크  
**장점**:
- 가볍고 유연함
- 필요한 모듈만 선택적으로 추가 가능
- 배우기 쉬워 입문자에게 적합
- 자유도가 높아 커스터마이징 용이

**적합한 경우**:  
단순하거나 자유로운 설계가 필요한 프로젝트, 소규모 웹 앱 또는 REST API 서버

---

## 3. FastAPI
**특징**: 최신 비동기 웹 프레임워크, API 개발에 최적화됨  
**장점**:
- 빠른 성능 (Starlette 기반의 비동기 처리)
- 자동 문서화 (Swagger UI 및 ReDoc 지원)
- Python 타입 힌팅 기반의 직관적인 코드 작성
- 비동기 함수 (`async/await`) 지원

**적합한 경우**:  
REST API 개발, 비동기 처리가 필요한 고성능 웹 서비스, 모바일 앱 백엔드 등

---

## 📊 프레임워크 비교 요약표

| 항목             | Django                        | Flask                        | FastAPI                           |
|------------------|-------------------------------|------------------------------|------------------------------------|
| **프레임워크 유형** | Full-Stack                    | 마이크로 프레임워크          | 경량 API 프레임워크               |
| **경량성**         | ❌ 무거움                      | ✅ 매우 가벼움                 | ✅ 비교적 가벼움                   |
| **성능**           | 중간                          | 느림                          | ✅ 매우 빠름 (비동기 기반)         |
| **비동기 지원**     | 제한적                        | ❌ 미지원                     | ✅ 완전 지원 (`async/await`)       |
| **자동 문서화**     | ❌ 없음                       | ❌ 없음                        | ✅ Swagger UI, ReDoc 자동 생성     |
| **기본 제공 기능** | 관리자, ORM, 인증, 보안 등 내장 | 최소 기능만 포함              | 라우팅, 타입검사 중심, 경량 구조   |
| **적합한 대상**     | 대규모 웹 서비스               | 소규모 앱, 자유로운 설계       | REST API 서버, 고성능 서비스       |

---

## 📌 추가 개념 설명

### 🔋 "배터리가 포함된" 프레임워크란?
"**Batteries Included**"는 Django의 철학으로,  
웹 개발에 필요한 주요 기능(인증, ORM, 관리자, 폼 처리, 보안 등)이 기본으로 내장되어 있어 별도의 설정이나 외부 라이브러리 없이도 실용적인 웹 서비스를 빠르게 구축할 수 있다는 의미입니다.

---

### 🔗 API란?
**API (Application Programming Interface)**는  
서로 다른 소프트웨어나 시스템이 데이터를 주고받기 위한 **표준화된 인터페이스**입니다.  
웹에서는 보통 **REST API** 형식으로 JSON 데이터를 HTTP 요청/응답으로 주고받습니다.

예시:
- `/users/1` → 사용자 1번 정보 조회
- `/posts` → 글 목록 가져오기

---

### 🧱 ORM이란?
**ORM (Object-Relational Mapping)**은  
데이터베이스의 테이블을 객체 지향 언어의 **클래스**와 **인스턴스**로 매핑하여,  
SQL을 직접 작성하지 않고도 데이터를 다룰 수 있게 해주는 기술입니다.

예시 (Django ORM):

```python
# Python 코드로 DB 행 추가
Article.objects.create(title="Hello", content="This is ORM")

# SQL 없이도 조회 가능
articles = Article.objects.filter(title__contains="Hello")
```