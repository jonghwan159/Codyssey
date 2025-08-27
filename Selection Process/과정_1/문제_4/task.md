# Windows Terminal 또는 Git Bash에서 실행

# 사용자 정보 설정
git config --global user.name "jonghwan159"
git config --global user.email "whdghks1999@naver.com"

# 줄바꿈 설정 (Windows 기준)
git config --global core.autocrlf true

# 기본 브랜치명을 main으로 설정 (Git 2.28 이상)
git config --global init.defaultBranch main

# 기본 에디터를 VSCode로 설정
git config --global core.editor "code --wait"

# 설정 목록 보기
git config --list

# 설정 파일 직접 열기
git config --global --edit


# 확인법
1. Git 설치 여부 확인

git --version

2. 개행문자 설정

git config --global core.autocrlf

3. 사용자 이름과 이메일 설정

git config --global user.name
git config --global user.email

4. 기본 브랜치 이름 main으로 변경

git config --global init.defaultBranch

5. 전역 설정 목록 확인

git config --global --list

6. 에디터에서 전역 설정 파일 띄우기

git config --global --edit

7. 기본 에디터를 VSCode로 변경

git config --global core.editor