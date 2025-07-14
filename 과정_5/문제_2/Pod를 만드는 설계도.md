```markdown
# 🧭 Kubernetes 선언형 실습: Pod → YAML → Service → 브라우저 접속

---

## ✅ 1단계: Pod 객체 설명 확인

```bash
kubectl explain pod
```

- Pod에서 설정할 수 있는 필드 구조가 나옴 (참고용)

---

## ✅ 2단계: 기존 hellok8s Pod의 YAML 내용 보기

```bash
kubectl get pod hellok8s -o yaml
```

- 이미 명령형으로 만든 Pod의 YAML 형식이 궁금할 때 사용

---

## ✅ 3단계: 선언형 YAML 파일 직접 만들기

```bash
nano hellok8s.yaml
```

- 아래 내용 붙여넣기:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: hellok8s-yaml
  labels:
    app: helloworld
spec:
  containers:
  - name: nginx
    image: nginx
    ports:
    - containerPort: 80
```

- 저장: `Ctrl + O` → `Enter`  
- 종료: `Ctrl + X`

---

## ✅ 4단계: YAML 문법 확인하고 싶으면 여기 참고 (선택)

- YAML 문법 검사기: [https://codebeautify.org/yaml-validator](https://codebeautify.org/yaml-validator)  
- YAML ↔ JSON 변환기: [https://codebeautify.org/yaml-to-json-xml-csv](https://codebeautify.org/yaml-to-json-xml-csv)

---

## ✅ 5단계: YAML 파일을 Kubernetes에 적용

```bash
kubectl apply -f hellok8s.yaml
```

---

## ✅ 6단계: 생성된 Pod 목록 및 상태 확인

```bash
kubectl get pods
kubectl describe pod hellok8s-yaml
```

---

## ✅ 7단계: 브라우저에서 접속할 수 있도록 Service 생성 (NodePort)

```bash
kubectl expose pod hellok8s-yaml --type=NodePort --port=80 --name=hellok8s-yaml
```

---

## ✅ 8단계: Service 목록 및 상세 정보 확인

```bash
kubectl get svc
kubectl describe svc hellok8s-yaml
```

- 여기서 NodePort 번호 확인 (예: `30080` 같은 숫자)

---

## ✅ 9단계: 웹브라우저 접속

브라우저 주소창에 아래처럼 입력:

```
http://localhost:<노드포트>
```

예시:

```
http://localhost:30080
```

---

## ✅ 10단계: 리소스 정리 (Pod, Service 삭제)

```bash
kubectl delete pod hellok8s
kubectl delete pod hellok8s-yaml
kubectl delete svc hellok8s-yaml
```

---

## 🎁 보너스: NodePort vs ClusterIP 차이

| 항목             | ClusterIP                | NodePort                        |
|------------------|---------------------------|----------------------------------|
| 기본값           | ✅                        | ❌                               |
| 접근 가능 범위   | 클러스터 내부만 접근 가능 | 외부 브라우저에서도 접속 가능   |
| 사용 목적        | 백엔드 통신               | 사용자가 직접 웹으로 접근       |
| 사용 예시        | 마이크로서비스 간 연결    | 웹 브라우저에서 페이지 확인     |
```
