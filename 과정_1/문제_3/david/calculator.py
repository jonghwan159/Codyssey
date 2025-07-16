def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero."
    return a / b

def evaluate_expression(expr):
    try:
        tokens = expr.strip().split()
        if len(tokens) != 3:
            return "Invalid input format. Use: number operator number"

        a, op, b = tokens
        a = int(a)
        b = int(b)

        if op == '+':
            return f"Result: {add(a, b)}"
        elif op == '-':
            return f"Result: {subtract(a, b)}"
        elif op == '*':
            return f"Result: {multiply(a, b)}"
        elif op == '/':
            return f"Result: {divide(a, b)}"
        else:
            return "Invalid operator."
    except ValueError:
        return "Invalid input. Please enter integers only."

if __name__ == "__main__":
    mode = input("Choose mode (1: step-by-step, 2: one-line expression): ")

    if mode == '1':
        try:
            a = int(input("Enter first integer: "))
            b = int(input("Enter second integer: "))
            op = input("Enter operator (+, -, *, /): ")

            if op == '+':
                print("Result:", add(a, b))
            elif op == '-':
                print("Result:", subtract(a, b))
            elif op == '*':
                print("Result:", multiply(a, b))
            elif op == '/':
                print("Result:", divide(a, b))
            else:
                print("Invalid operator.")
        except ValueError:
            print("Invalid input. Please enter valid integers.")

    elif mode == '2':
        expr = input("Enter expression: ")
        print(evaluate_expression(expr))
    else:
        print("Invalid mode selected.")
