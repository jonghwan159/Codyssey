# 🧭 Kubernetes 명령형 실습: Pod 생성 → 포트 노출 → 브라우저 확인

---

## ✅ 1단계: Docker Desktop에서 Kubernetes 활성화
- Docker Desktop 실행 → Settings → Kubernetes → "Enable Kubernetes" 체크 → Apply & Restart

---

## ✅ 2단계: 명령형 방식으로 Pod 생성

```bash
kubectl run hellok8s --image=nginx --port=80
```

- Pod 이름: `hellok8s`
- 이미지: `nginx` (Docker Hub에서 가져옴)
- 포트: `80`

---

## ✅ 3단계: 생성된 Pod 목록 확인

```bash
kubectl get pods
```

---

## ✅ 4단계: Pod 상세 정보 확인

```bash
kubectl describe pod hellok8s
```

---

## ✅ 5단계: kubectl port-forward 명령으로 포트 노출

```bash
kubectl port-forward pod/hellok8s 8080:80
```

- 브라우저에서 접속 주소:
```
http://localhost:8080
```

- 이 명령은 터미널을 점유하므로, 새 터미널을 열어야 다른 명령어 사용 가능

---

## ✅ 6단계: 웹브라우저에서 확인
- 위에서 연 `http://localhost:8080` 주소로 접속 시 nginx 환영 페이지가 보여야 정상

---

## ✅ 7단계: 포트 포워딩 중지
- `Ctrl + C` 입력해서 종료

---

## ✅ 8단계: 리소스 정리 (선택)

```bash
kubectl delete pod hellok8s
```