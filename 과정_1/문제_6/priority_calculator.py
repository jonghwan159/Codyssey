# 기본 사칙연산 함수
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # 0으로 나누는 경우 예외 발생
    if b == 0:
        raise ZeroDivisionError
    return a / b

# 연산자 우선순위 정의 (값이 높을수록 우선순위 높음)
precedence = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2
}

# 연산자 적용 함수 (순서 중요: a op b)
def apply_operator(op, b, a):
    if op == '+':
        return add(a, b)
    elif op == '-':
        return subtract(a, b)
    elif op == '*':
        return multiply(a, b)
    elif op == '/':
        return divide(a, b)

# 수식 계산 함수
def calculate(tokens):
    try:
        nums = []  # 숫자 스택
        ops = []   # 연산자 스택
        i = 0

        while i < len(tokens):
            token = tokens[i]

            if token == '(':
                # 여는 괄호는 연산자 스택에 바로 추가
                ops.append(token)

            elif token == ')':
                # 닫는 괄호가 나올 때까지 연산 수행
                while ops and ops[-1] != '(':
                    op = ops.pop()
                    b = nums.pop()
                    a = nums.pop()
                    nums.append(apply_operator(op, b, a))
                if not ops:
                    return "Invalid input."  # 괄호 짝 안 맞음
                ops.pop()  # '(' 제거

            elif token in precedence:
                # 현재 연산자의 우선순위보다 높거나 같은 연산자 먼저 계산
                # 앞에 있는 연산자가 우선순위가 높을 때 실행
                while (ops and ops[-1] in precedence and
                       precedence[ops[-1]] >= precedence[token]):
                    op = ops.pop()
                    b = nums.pop()
                    a = nums.pop()
                    nums.append(apply_operator(op, b, a))
                ops.append(token)  # 현재 연산자 스택에 추가

            else:
                # 숫자는 float으로 변환해서 숫자 스택에 추가
                nums.append(float(token))

            i += 1

        # 남은 연산자 처리
        # 뒤에 있는 연산자가 우선순위 높을 때 처리
        while ops:
            if ops[-1] == '(' or ops[-1] == ')':
                return "Invalid input."
            op = ops.pop()
            b = nums.pop()
            a = nums.pop()
            nums.append(apply_operator(op, b, a))

        # 최종 결과 반환
        return nums[0]

    except ZeroDivisionError:
        return "Error: Division by zero."
    except:
        return "Invalid input."

# 프로그램 시작점
def main():
    expr = input("Enter expression: ").strip()  # 사용자 입력
    tokens = expr.split()  # 공백 기준 토큰 분리
    if not tokens:
        print("Invalid input.")
        return
    result = calculate(tokens)  # 계산 실행
    print("Result:", result)

# 메인 함수 호출 조건
if __name__ == "__main__":
    main()
