def main():
    try:
        nums = input("Enter numbers: ").split()
        numbers = [float(n) for n in nums]

        min_val = numbers[0]
        max_val = numbers[0]

        for n in numbers[1:]:
            if n < min_val:
                min_val = n
            if n > max_val:
                max_val = n

        print(f"Min: {min_val}, Max: {max_val}")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
