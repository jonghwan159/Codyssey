def main():
    try:
        # 숫자와 지수 입력 받기
        number = float(input("Enter number: "))
        exponent = int(input("Enter exponent: "))
        
        # 거듭제곱 계산
        result = 1
        for _ in range(abs(exponent)):
            result *= number
        
        # 지수가 음수일 경우, 결과를 반전
        if exponent < 0:
            result = 1 / result
        
        print(f"Result: {result}")

    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()

