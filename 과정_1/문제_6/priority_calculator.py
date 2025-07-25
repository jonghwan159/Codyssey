def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b

def calculate(tokens):
    try:
        # 숫자 변환
        values = []
        operators = []

        # 1단계: *, / 먼저 처리
        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token in ('*', '/'):
                a = float(values.pop())
                b = float(tokens[i + 1])
                if token == '*':
                    values.append(multiply(a, b))
                else:
                    values.append(divide(a, b))
                i += 2
            elif token in ('+', '-'):
                operators.append(token)
                values.append(float(tokens[i - 1]) if i == 0 else float(tokens[i + 1]))
                i += 2
            else:
                if i == 0 or tokens[i - 1] in ('+', '-'):
                    values.append(float(token))
                    i += 1
                else:
                    i += 1

        # 2단계: +, - 처리
        result = values[0]
        for idx, op in enumerate(operators):
            if op == '+':
                result = add(result, values[idx + 1])
            else:
                result = subtract(result, values[idx + 1])

        return result
    except ZeroDivisionError:
        return "Error: Division by zero."
    except:
        return "Invalid input."

def main():
    expr = input("Enter expression: ").strip()
    tokens = expr.split()
    if not tokens:
        print("Invalid input.")
        return
    result = calculate(tokens)
    print("Result:", result)

if __name__ == "__main__":
    main()
