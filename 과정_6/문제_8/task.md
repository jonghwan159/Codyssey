# 🚀 Kubernetes 실습 과제: PVC 생성 및 정보 조회

## ✅ 1단계: mysql-pv-claim 생성 (명령형 또는 선언형)
mysql-pvc.yaml
```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: mysql-pv-claim
  labels:
    app: wordpress
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 20Gi
```

```bash
kubectl apply -f mysql-pvc.yaml
```

## ✅ 2단계: wp-pv-claim 생성
wp-pvc.yaml

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: wp-pv-claim
  labels:
    app: wordpress
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 20Gi
```
```bash
kubectl apply -f wp-pvc.yaml
```

## ✅ 3단계: PV와 PVC 목록 조회
```bash
kubectl get pv
kubectl get pvc
```

## ✅ 4단계: 각 PV, PVC 상세 정보 확인
```bash
kubectl describe pvc mysql-pv-claim
kubectl describe pvc wp-pv-claim
```
(※ PV는 동적으로 바인딩되었는지에 따라 자동 생성되거나 수동으로 생성 필요)

# 🎁 보너스 과제 정리

## ✅ AccessMode 종류와 특징

| AccessMode     | 설명                                                  |
|----------------|-------------------------------------------------------|
| ReadWriteOnce  | 단일 노드에서 읽기/쓰기 가능 (대부분의 경우 사용)    |
| ReadOnlyMany   | 여러 노드에서 동시에 읽기 가능                        |
| ReadWriteMany  | 여러 노드에서 동시에 읽기/쓰기 가능 (NFS 등 필요)     |

---

## ✅ PVC와 PV의 역할

| 리소스 | 설명                                                       |
|--------|------------------------------------------------------------|
| PV (PersistentVolume)  | 클러스터 관리자가 사전에 정의한 실제 저장소 리소스        |
| PVC (PersistentVolumeClaim) | 사용자가 요청하는 저장소 요구사항 (크기, AccessMode 등) |

> PVC는 PV를 "요청"하는 방식이며, 바인딩되면 실제 볼륨을 사용 가능하게 됩니다.

---

## ✅ PV의 볼륨 타입과 특징

| 타입                         | 설명                                       |
|------------------------------|--------------------------------------------|
| hostPath                     | 노드의 디렉토리를 사용 (단일 노드 테스트용) |
| nfs                          | NFS 서버 공유 디스크 사용                   |
| gcePersistentDisk / awsElasticBlockStore | 클라우드 환경의 디스크 볼륨              |
| emptyDir                     | Pod가 실행되는 동안 임시 디렉토리 제공       |
| local                        | 특정 노드에 있는 로컬 디스크 사용           |
| persistentVolumeClaim        | 다른 PVC를 참조하여 생성된 PV              |


🟢 모든 리소스를 확인하려면:

```bash
kubectl get all,pv,pvc
```
필요하면 kubectl delete pvc <이름> 으로 삭제 가능!