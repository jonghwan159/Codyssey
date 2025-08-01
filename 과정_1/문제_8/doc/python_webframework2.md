# Python 웹 프레임워크 - Flask

## 1. **Run Without Debugging vs Start Debugging 차이점**

- **Run Without Debugging**:
  - 코드를 디버깅 없이 실행합니다.
  - 프로그램이 실행되고, 오류가 발생하지 않으면 자동으로 종료됩니다.
  - **디버깅 도구**가 활성화되지 않으며, 애플리케이션의 실행 상태를 추적하거나 중단점 등을 사용할 수 없습니다.
  
- **Start Debugging**:
  - 코드 실행을 **디버깅 모드**로 실행합니다.
  - 애플리케이션을 실행하면서 중단점을 설정하고, 변수 값을 추적하는 등의 디버깅 작업을 할 수 있습니다.
  - 코드 실행 중에 **오류가 발생하면** 디버깅을 통해 문제를 추적할 수 있습니다.

## 2. **Flask의 역할 요약**

**Flask**는 **Python**으로 작성된 경량화된 웹 프레임워크입니다. 주요 특징은 다음과 같습니다:
- **간단한 API 제공**: 빠르게 웹 애플리케이션을 개발할 수 있도록 다양한 기능을 제공.
- **라우팅**: 사용자가 요청한 URL에 대해 적절한 처리를 해주는 라우팅 기능.
- **템플릿 렌더링**: HTML 페이지와 데이터를 결합하여 웹 페이지를 동적으로 생성할 수 있도록 함.
- **확장성**: 필요에 따라 다양한 플러그인을 추가할 수 있어 **유연한 확장성** 제공.
- **RESTful API**를 쉽게 구축할 수 있도록 지원.

Flask는 초보자에게 적합한 웹 프레임워크로, 프로젝트가 커짐에 따라 **Django**와 같은 보다 복잡한 프레임워크로 전환할 수 있는 좋은 시작점이 됩니다.

## 3. **0.0.0.0으로 설정 시 의미와 장단점**

- **`0.0.0.0`**:
  - 모든 네트워크 인터페이스에서 접근할 수 있도록 설정하는 것입니다. 즉, **내부 네트워크뿐만 아니라 외부에서도 애플리케이션에 접근할 수 있게 됩니다.**
  
- **장점**:
  - 다른 장치나 컴퓨터에서 애플리케이션에 접근할 수 있어, 로컬 환경이 아니라도 서버 테스트가 가능.
  
- **단점**:
  - **보안 위험**이 있을 수 있습니다. 외부에서 서버에 접근할 수 있기 때문에 **방화벽**이나 **인증**을 설정하지 않으면 보안 문제가 발생할 수 있습니다.
  - 기본적으로 **디버깅 모드**에서는 보안에 취약할 수 있으므로 **실제 배포 환경에서는 사용하지 않는 것이 좋습니다.**

## 4. **127.0.0.1 접속 vs 내부 IP 접속 차이**

- **127.0.0.1 (localhost)**:
  - **로컬 머신**에서만 접근할 수 있는 IP 주소입니다. 즉, **내 컴퓨터**에서만 접속이 가능합니다.
  
- **내부 IP**:
  - **같은 네트워크 내 다른 컴퓨터**에서 접속할 수 있는 주소입니다.
  - 예를 들어, 같은 로컬 네트워크 내에서 다른 컴퓨터가 이 서버에 접근하려면 서버의 **내부 IP 주소**를 통해 접속해야 합니다.

**차이점**:
- **127.0.0.1**은 **로컬**에서만 접속 가능하지만, **내부 IP**는 **같은 네트워크 내의 다른 장치**에서 접속할 수 있습니다.

## 5. **포트 번호의 의미와 기본 충돌 시 해결 방안**

- **포트 번호의 의미**:
  - **포트 번호**는 애플리케이션이 사용하는 **네트워크 채널**을 정의합니다.
  - 예를 들어, **HTTP**는 기본적으로 **80번 포트**, **HTTPS**는 **443번 포트**를 사용합니다.
  - Flask와 같은 개발 서버는 기본적으로 **5000번 포트**를 사용합니다.
  
- **포트 충돌 시 해결 방안**:
  - **포트 충돌**은 이미 다른 프로세스가 해당 포트를 사용 중일 때 발생합니다.
  - 이를 해결하려면:
    1. **다른 포트**로 변경:
       ```python
       app.run(host="0.0.0.0", port=5001)
       ```
    2. 사용 중인 포트를 확인하고 종료하기:
       ```bash
       lsof -i :5000
       kill <PID>
       ```

## 6. **문서 제출 항목**

### 1. 웹 환경 테스트 (app.py)

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, DevOps!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
