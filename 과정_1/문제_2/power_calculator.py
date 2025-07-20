def main():
    try:
        number = float(input("Enter number: "))
    except ValueError:
        print("Invalid number input.")
        return

    try:
        exponent = int(input("Enter exponent: "))
    except ValueError:
        print("Invalid exponent input.")
        return

    result = 1
    for _ in range(abs(exponent)):
        result *= number

    if exponent < 0:
        result = 1 / result

    # 결과물 정수 유무에 따른 처리
    if result.is_integer():
        print(f"Result: {int(result)}")
    else:
        print(f"Result: {result}")

if __name__ == "__main__":
    main()