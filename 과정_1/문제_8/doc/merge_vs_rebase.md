# merge_vs_rebase.md

## Merge vs Rebase 차이점

- **Merge**는 브랜치 히스토리를 그대로 유지하며 새로운 커밋으로 병합합니다.
- **Rebase**는 브랜치를 현재 브랜치의 HEAD로 이동시켜 커밋 히스토리를 깔끔하게 재작성합니다.

## 협업에서 Merge를 추천하는 이유

- Merge는 이력이 명확하게 남기 때문에 협업 중 누가 어떤 작업을 했는지 추적하기 쉽습니다.
- 충돌 발생 시 어떤 브랜치에서 충돌이 발생했는지 알기 쉬워서 팀 내 커뮤니케이션이 용이합니다.
