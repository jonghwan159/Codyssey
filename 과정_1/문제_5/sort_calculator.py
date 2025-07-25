# 버블 정렬 함수 정의
def bubble_sort(arr):
    n = len(arr)
    # 리스트의 길이만큼 반복
    for i in range(n):
        # 이미 정렬된 부분은 제외하고 반복
        for j in range(0, n - i - 1):
            # 현재 원소가 다음 원소보다 크면 자리 바꿈 (오름차순 정렬)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    # 정렬된 리스트 반환
    return arr

# 프로그램의 메인 실행 함수
def main():
    try:
        # 사용자에게 숫자 입력 받기 (공백 구분)
        raw_input = input("Enter numbers: ").strip()

        # 입력이 비어 있으면 예외 발생
        if not raw_input:
            raise ValueError

        # 입력된 문자열을 공백 기준으로 나눠 리스트로 저장
        str_nums = raw_input.split()

        # 각각을 float로 변환 (숫자가 아니면 ValueError 발생)
        nums = [float(x) for x in str_nums]

        # 버블 정렬 함수로 숫자 리스트 정렬
        sorted_nums = bubble_sort(nums)

        # 결과를 공백으로 구분된 문자열로 출력
        print("Sorted:", ' '.join([str(x) for x in sorted_nums]))

    # 예외 발생 시 (빈 입력이거나 숫자가 아닌 값이 포함되었을 경우)
    except ValueError:
        print("Invalid input.")

# 메인 함수 실행 조건 (이 스크립트를 직접 실행할 때만 실행됨)
if __name__ == "__main__":
    main()
