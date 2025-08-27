# Kubernetes 실습 과제: david 이미지로 Pod 실행 및 Service 생성

---

## ✅ 1단계: david Pod 실행 (명령형 방식)

```bash
kubectl run david --image=jonghwan159/david:v1.0 --port=80 --labels="app=david"
```
- --image=jonghwan159/david:v1.0: DockerHub에서 v1.0 태그 사용

- --labels="app=david": label 설정

## ✅ 2단계: 포트 포워딩으로 웹 브라우저 확인
```bash
kubectl port-forward pod/david 8080:80
```
- 브라우저에서 http://localhost:8080 접속하여 확인

- 확인 후 Ctrl+C로 포워딩 종료

## ✅ 3단계: Service 정의 (선언형 방식)
service.yaml
```yaml
apiVersion: v1
kind: Service
metadata:
  name: david-svc
  labels:
    app: david
spec:
  selector:
    app: david
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
  type: NodePort
  ```
```bash
kubectl apply -f service.yaml
```
## ✅ 4단계: 서비스 확인
```bash
kubectl get svc
kubectl describe svc david-svc
```
- 할당된 NodePort 확인 후 http://localhost:NODEPORT 로 접속

## ✅ 5단계: Pod 및 Service 목록 확인
```bash
kubectl get pods
kubectl get svc
kubectl describe pod david
kubectl describe svc david-svc
```
## ✅ 6단계: Pod 정보를 yaml 형태로 출력 및 백업
``` bash
kubectl get pod david -o yaml > david_pod_backup.yaml
```
## ✅ 7단계: Pod 삭제 (Service는 유지)
```bash
kubectl delete pod david
```
## ✅ 8단계: Git에 커밋 및 푸시
```bash
git add .
git commit -m "feat/과정_6/문제_3"
git push origin main
```

# 🎁 보너스 과제 문서

## ✅ 포트 포워딩의 정의와 목적
포트 포워딩은 클러스터 내부에 존재하는 Pod나 Service의 포트를 로컬 머신 포트와 연결하는 기능이다.
보통 NodePort 없이도 빠르게 브라우저에서 Pod의 웹 서버를 확인할 때 유용하다.

##  ✅ Pod YAML 구조 분석
예시:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: david
  labels:
    app: david
spec:
  containers:
    - name: david
      image: jonghwan159/david:v1
      ports:
        - containerPort: 80
```
구조 설명:

- apiVersion, kind: 리소스 타입 정의

- metadata: 이름, 라벨 등 메타정보

- spec.containers: 컨테이너 설정

    - name, image, ports: 컨테이너 정의

## ✅ 명령형 vs 선언형 방식 차이
| 구분      | 명령형 (Imperative)             | 선언형 (Declarative)            |
|-----------|----------------------------------|----------------------------------|
| 사용 예   | `kubectl run`, `kubectl expose` | `kubectl apply -f`              |
| 특징      | 즉시 명령 실행                   | YAML 파일 기반 상태 선언        |
| 장점      | 빠른 테스트 및 단발 작업 용이    | 형상 관리 및 반복 실행 가능     |
| 단점      | 변경 이력 및 추적 어려움         | 초기 작성이 번거롭고 시간 소요  |


## ✅ Pod와 Service의 역할
- Pod: Kubernetes에서 가장 작은 배포 단위. 컨테이너를 실행하는 논리적 호스트.

- Service: Pod들의 네트워크 접근을 안정적으로 제공하는 추상 레이어.

    - ClusterIP: 클러스터 내부 통신용

    - NodePort: 외부 브라우저 접근 가능

🟢 모든 실습 완료 시 kubectl get all 명령어로 상태 점검!