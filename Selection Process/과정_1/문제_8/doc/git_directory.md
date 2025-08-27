# Git 보너스 과제 정리

## ✅ 버전 관리 시스템의 종류

1. **로컬 버전 관리 시스템 (Local VCS)**
   - 예: RCS
   - 개인 PC에서 파일 버전만 관리

2. **중앙 집중형 VCS (Centralized VCS)**
   - 예: SVN, CVS
   - 중앙 서버에서 버전 일괄 관리

3. **분산형 VCS (Distributed VCS)**
   - 예: Git, Mercurial
   - 클라이언트가 전체 저장소 복사본을 가짐

---

## ✅ `.git` 디렉토리의 역할

- Git 저장소의 핵심 정보 저장 위치
- 주요 구성:
  - `HEAD`: 현재 브랜치 참조
  - `config`: 저장소별 설정
  - `objects/`: 커밋, 트리, 블롭 등 데이터 저장
  - `refs/`: 브랜치와 태그 참조
  - `logs/`: 커밋 이력

---

## ✅ `.git` 삭제 및 복원 실험

1. `.git` 삭제 후 상태 확인:
```bash
rm -rf .git
git status
# 결과: fatal: not a git repository
