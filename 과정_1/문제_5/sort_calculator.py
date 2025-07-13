def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def main():
    try:
        raw_input = input("Enter numbers: ").strip()
        if not raw_input:
            raise ValueError

        str_nums = raw_input.split()
        nums = [float(x) for x in str_nums]

        sorted_nums = bubble_sort(nums)

        print("Sorted:", ' '.join([str(x) for x in sorted_nums]))

    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
