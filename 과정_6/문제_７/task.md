# 🚀 Kubernetes 실습 과제: Deployment replicas 변경 & Service 적용

## ✅ 1단계: 터미널 2개 띄우기
- 터미널 1: 실시간 Pod 상태 확인

- 터미널 2: replicas 조작 및 서비스 적용

## ✅ 2단계: 터미널 1에서 pod 상태 지속 출력
```bash
watch kubectl get pods
```
- watch 명령어는 Pod 상태가 실시간으로 변할 때마다 갱신해 보여줍니다.

    - 만약 watch 명령이 없다면 아래 대체:

    ```bash
    watch -n 1 kubectl get pods
    ```
## ✅ 3단계: 터미널 2에서 replicas를 1로 수정
```bash
kubectl scale deployment david-deployment --replicas=1
```
- 결과: Pod가 3개 → 1개로 줄어듦

## ✅ 4단계: Pod 개수 변화 확인
- 터미널 1에 실시간으로 표시됨

## ✅ 5단계: replicas를 다시 3으로 변경
```bash
kubectl scale deployment david-deployment --replicas=3
```
- 결과: 다시 Pod 3개 생성됨

## ✅ 6단계: service.yaml 파일로 Service 생성
service.yaml 파일 내용 예시:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: david-svc
  labels:
    app: david
spec:
  type: NodePort
  selector:
    app: david
  ports:
    - port: 80
      targetPort: 80
```
적용:

```bash
kubectl apply -f service.yaml
```

## ✅ 7단계: 서비스 목록 및 상세 정보 확인
```bash
kubectl get svc
kubectl describe svc david-svc
```
- NodePort 확인 후 외부 접속 준비

## ✅ 8단계: 파이어폭스에서 접속
```bash
minikube service david-svc --url
```

- 출력된 URL을 가상머신의 Firefox 브라우저에서 열면 됩니다!

🟢 최종 확인 명령어:

```bash
kubectl get all
```