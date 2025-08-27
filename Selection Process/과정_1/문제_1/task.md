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

