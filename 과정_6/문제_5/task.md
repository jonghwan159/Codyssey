# ✅ Minikube + Kubectl 설치 및 기초 실습

## ✅ 1단계: Minikube 설치 (v1.22.0)
```bash
curl -LO https://storage.googleapis.com/minikube/releases/v1.22.0/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
minikube version  # 버전 확인
```

## ✅ 2단계: kubectl 설치 (v1.22.1)
```bash
curl -LO "https://dl.k8s.io/release/v1.22.1/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/
kubectl version --client  # 클라이언트 버전 확인
```

## ✅ 3단계: minikube docker 드라이버 기반 시작
```bash
minikube start --driver=docker
```
- Docker 데몬을 기반으로 minikube 클러스터가 시작됨

- 도중 오류 발생 시 minikube delete 후 재시도

## ✅ 4단계: 가상머신 재부팅 후 상태 확인
```bash
minikube status  # 클러스터 상태 확인
minikube start   # 필요시 클러스터 재시작
```

## ✅ 5단계: Docker 컨테이너 전체 목록 확인
``` bash
docker ps -a
```

- 로컬 PC (또는 VM)의 Docker 컨테이너 전체 확인

## ✅ 6단계: minikube 내부로 SSH 접속
```bash
minikube ssh
```

- 내부는 경량 Linux 컨테이너 환경

## ✅ 7단계: minikube 내부에서 Docker 컨테이너 목록 확인
```bash
docker ps -a
```

> 이때 보이는 컨테이너는 minikube 내부에서 실행 중인 Kubernetes 구성요소임 (etcd, kube-apiserver 등)

## ✅ 8단계: minikube IP 확인
```bash
minikube ip
```

- 클러스터의 외부 접근 IP 주소 확인

- 이후 NodePort 서비스 등 외부 접근 시 사용

# 🎁 보너스 과제
## ✅ minikube 삭제 및 재시작
```bash
minikube delete
minikube start --driver=docker
```
- 전체 클러스터를 초기화 후 재시작

- 불필요한 리소스 정리 시 사용

## ✅ minikube 클러스터 구성 요약 그림
```markdown
[사용자 PC / VM]
└── minikube (docker driver 기반 Kubernetes 단일 노드 클러스터)
    ├── kube-apiserver
    ├── kube-controller-manager
    ├── kube-scheduler
    ├── etcd
    └── 컨테이너(Pod)를 실행하는 Docker (컨테이너 런타임)
-> 단일 VM 안에 모든 Kubernetes 컴포넌트가 구성됨 (개발/테스트용)
```

## ✅ 모든 단계를 완료한 후, 아래 명령으로 클러스터 정상 작동 여부를 최종 확인:

```bash
kubectl get nodes
kubectl get pods -A
```