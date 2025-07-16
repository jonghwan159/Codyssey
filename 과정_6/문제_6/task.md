# 🚀 Kubernetes 실습 과제: minikube 기반 Pod 접근
## ✅ 1단계: minikube 상태 확인 및 시작
```bash
minikube status
```
- 상태가 Stopped면 아래 명령어로 시작:

```bash
minikube start --driver=docker
```
## ✅ 2단계: Git 저장소에서 코드 내려받기
```bash
git clone https://github.com/jonghwan159/Codyssey.git
cd Codyssey
git checkout main
```
## ✅ 3단계: deployment.yaml 적용
```bash
kubectl apply -f deployment.yaml
```
## ✅ 4단계: Pod 목록 및 IP 확인
```bash
kubectl get pods -o wide
```
- IP는 IP 열에서 확인 가능

## ✅ 5단계: Deployment 목록 확인
```bash
kubectl get deployments
```

## ✅ 6단계: Pod, Deployment 상세 정보 확인
```bash
kubectl describe pod <pod-name>
kubectl describe deployment david-deployment
```

## ✅ 7단계: 특정 Pod IP로 ping, curl 요청 (로컬에서)
```bash
ping <POD_IP>           # 성공 안 될 수 있음
curl http://<POD_IP>    # 실패 가능
```

## ✅ 8단계: minikube ssh로 접속 후 ping, curl
```bash
minikube ssh
ping <POD_IP>
curl http://<POD_IP> 
exit
```

## ✅ 9단계: 포트 포워딩 후 로컬 PC 브라우저 접속
```bash
kubectl port-forward pod/<pod-name> 8080:80
```

- 브라우저에서 http://localhost:8080 접속

- 종료는 Ctrl + C

# 🎁 보너스 과제 문서

## ✅ Pod IP로 minikube 외부에서 접속되지 않는 이유
Kubernetes의 Pod는 클러스터 내부 네트워크를 사용하기 때문에, PC 또는 외부 환경에서는 직접 접근이 불가능합니다. Pod의 IP는 일반적으로 가상 네트워크 내의 IP로, 호스트 네트워크에서 라우팅할 수 없습니다.

## ✅ 포트포워딩을 사용하는 이유
kubectl port-forward는 로컬 PC의 포트를 Pod의 포트에 직접 연결해줍니다.
이를 통해 서비스(Service)나 NodePort 없이도 간단하게 테스트할 수 있어 개발 단계에서 매우 유용합니다.

- ✅ 빠르게 웹 브라우저로 확인 가능

- ✅ 클러스터 내부 구조 노출 없이 접근 가능

- ✅ Service 없이도 디버깅 용이

🟢 모든 실습이 완료되면 아래로 전체 리소스 확인 가능:

```bash
kubectl get all
```