# Kubernetes 실습 과제: Deployment로 david Pod 3개 생성

## ✅ 1단계: .dockerignore 파일 수정
작업 디렉토리의 .dockerignore 파일에 다음 내용을 추가합니다:
```bash
service.yaml
deployment.yaml
```

## ✅ 2단계: deployment.yaml 파일 작성
deployment.yaml
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: david-deployment
  labels:
    app: david
spec:
  replicas: 3
  selector:
    matchLabels:
      app: david
  template:
    metadata:
      labels:
        app: david
    spec:
      containers:
        - name: david
          image: jonghwan159/david:v1.0
          ports:
            - containerPort: 80
```

## ✅ 3단계: Deployment 생성
```bash
kubectl apply -f deployment.yaml
```
## ✅ 4단계: Pod 목록 변화 확인
```bash
kubectl get pods --watch
```
- 총 3개의 david Pod가 모두 Running 상태가 될 때까지 확인

## ✅ 5단계: Deployment 목록 확인
```bash
kubectl get deployments
```

## ✅ 6단계: 상세 정보 확인
```bash
kubectl describe deployment david-deployment
kubectl describe pods
```

## ✅ 7단계: 브라우저에서 서비스 확인
> 기존에 생성한 david-svc 서비스 유지

```bash
kubectl get svc
```
- 브라우저 접속: http://localhost:<NodePort>

## ✅ 8단계: Pod 내부에 bash로 접속해 파일 유무 확인
```bash
kubectl exec -it <david-pod-name> -- bash
cd /app
ls
```
- service.yaml, deployment.yaml 파일이 없어야 합니다.
(없다면 .dockerignore 파일이 제대로 작동한 것)

✅ 마무리 점검 명령어

```bash
kubectl get all
```

## ✅ 9단계: Git 커밋 및 푸시
```bash
git add .
git commit -m "feat/과정_6/문제_4"
git push origin main
```
# 🎁 보너스 과제 문서

## ✅ Deployment와 ReplicaSet의 역할
| 리소스       | 설명                                                                 |
|--------------|----------------------------------------------------------------------|
| Deployment   | 선언한 상태를 유지하도록 Pod를 관리하는 상위 리소스. ReplicaSet을 생성 및 관리 |
| ReplicaSet   | 지정된 수의 Pod 복제본을 유지하는 리소스. Pod 수를 자동으로 맞춰줌           |

- Deployment는 직접 Pod를 생성하지 않고, 내부적으로 ReplicaSet을 생성해서 원하는 개수의 Pod를 유지합니다.

- 사용자는 deployment.yaml만 관리하고, Kubernetes가 자동으로 ReplicaSet과 Pod를 조정합니다.
