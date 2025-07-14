
# 📦 보너스 과제: Kubernetes와 컨테이너 오케스트레이션

---

## ✅ 0. 컨테이너와 Docker란?

### 🔹 컨테이너란?
컨테이너는 애플리케이션과 그 실행에 필요한 모든 파일(코드, 라이브러리, 설정 등)을 하나로 패키징한 **독립된 실행 환경**입니다.  
"내 컴퓨터에선 되는데 서버에선 안 돼요"를 해결하기 위해 만들어졌습니다.  
**가상 머신보다 가볍고 빠르며**, 어디서든 **일관된 실행 환경**을 제공합니다.

### 🔹 Docker란?
Docker는 컨테이너를 **만들고, 실행하고, 공유할 수 있게 해주는 도구**입니다.  
`docker run`, `docker build`, `docker pull` 같은 명령어로 애플리케이션을 컨테이너로 실행할 수 있습니다.  
Kubernetes는 이러한 Docker 컨테이너들을 자동으로 관리하는 역할을 합니다.

---

## ✅ 1. 컨테이너 오케스트레이션의 정의

컨테이너 오케스트레이션은 여러 개의 컨테이너를 **자동으로 배치, 관리, 확장, 복구**하는 기술입니다.  
대규모의 컨테이너 기반 애플리케이션을 효율적으로 운영하기 위해 사용됩니다.  
Kubernetes는 대표적인 오케스트레이션 도구로, 개발자가 원하는 상태(desired state)를 선언하면 클러스터가 자동으로 이를 유지해줍니다.

---

## ✅ 2. Kubernetes 아키텍처 그림과 설명

### 📌 구성요소

#### 🔹 컨트롤 플레인 (Control Plane)
- **API Server**: Kubernetes 클러스터의 진입점. 모든 명령은 여기로 들어감.
- **Scheduler**: 새로 생성된 Pod를 적절한 Node에 할당.
- **Controller Manager**: 클러스터 상태를 지속적으로 감시하고 필요한 변경 수행.
- **etcd**: 모든 클러스터 상태를 저장하는 분산 키-값 저장소.

#### 🔹 워커 노드 (Worker Node)
- **kubelet**: Node에서 Pod를 실행하고 상태 보고.
- **kube-proxy**: 클러스터 내부 네트워크 트래픽 라우팅.
- **Container Runtime**: 실제 컨테이너를 실행하는 소프트웨어 (예: containerd, Docker 등)

> 아키텍처 이미지 참고: https://kubernetes.io/ko/docs/concepts/overview/components/

---

## ✅ 3. 컨테이너 오케스트레이션 종류 (CNCF Landscape 기준)

1. **Kubernetes**  
   가장 널리 사용되는 오케스트레이션 도구. 커뮤니티 중심, 클라우드 친화적, 확장성 우수.

2. **Docker Swarm**  
   Docker에서 자체 제공하는 오케스트레이션. 설정은 간단하지만 확장성과 유연성은 부족.

3. **Apache Mesos + Marathon**  
   분산 시스템 운영에 적합. 대규모 배포에 강점이 있으나 복잡함.

---

## ✅ 4. Kubernetes 배포판 종류와 사용 목적

1. **Minikube**  
   로컬 개발용 Kubernetes 클러스터. 가벼운 실습 및 테스트에 적합.

2. **Amazon EKS (Elastic Kubernetes Service)**  
   AWS에서 제공하는 완전관리형 K8s 서비스. 인프라 관리 최소화.

3. **Rancher**  
   멀티 클러스터 관리, UI 기반 운영에 강점. 사내 또는 하이브리드 클라우드 운영에 적합.


