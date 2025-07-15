# ✅ DockerHub 업로드 실습 정리

## 1. DockerHub 계정 가입 및 토큰 생성
- https://hub.docker.com 접속 후 회원가입
- [Account Settings] → [Security] → settings/personal-access-tokens → Generate New Token
- 생성된 토큰은 복사해두기 (비밀번호 대신 사용됨)

## 2. DockerHub 로그인 
```bash
docker login
(토큰사용시 아래 명령어 추가로 실행)
Username: <DockerHub 사용자명>
Password: <복사한 토큰>
```

## 3. DockerHub에 저장소 생성 (홈페이지에서 실행)
- 저장소 이름: david

- 설정: Public (기본값 유지)

## 4. 로컬 이미지 태그 설정 (도커허브에 업로드용)
```bash
docker tag david:v1.0 <DockerHub 사용자명>/david:v1.0
```
예시:

```bash
docker tag david:v1.0 jonghwan159/david:v1.0
```

## 5. DockerHub에 이미지 푸시
```bash
docker push <DockerHub 사용자명>/david:v1.0
```
예시:

```bash
docker push jonghwan159/david:v1.0
```
# 🏅 보너스 과제

## 📌 DockerHub를 사용하는 이유

| 항목             | 설명                                                  |
|------------------|-------------------------------------------------------|
| 표준화된 저장소 | 다양한 OS/언어 기반의 Official Image 제공             |
| CI/CD 연동 용이  | GitHub Actions, Jenkins 등과 연계 가능                 |
| 공유 및 협업     | Public 이미지 공유를 통한 협업 용이                    |
| 보안 토큰 관리   | Access Token 기반의 안전한 로그인 제공                 |

## 📦 Container Registry 종류 (3가지)

| 종류                            | 설명                                                  |
|---------------------------------|-------------------------------------------------------|
| DockerHub                       | 가장 널리 사용되는 기본 퍼블릭 컨테이너 저장소         |
| GitHub Container Registry (GHCR) | GitHub에서 제공하는 CI/CD 연계 이미지 저장소          |
| Amazon Elastic Container Registry (ECR) | AWS에서 제공하는 프라이빗 이미지 저장소    |
