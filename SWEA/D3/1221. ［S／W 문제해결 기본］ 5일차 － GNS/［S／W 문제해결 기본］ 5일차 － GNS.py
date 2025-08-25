# GNS 문제를 위한 버블 정렬 함수 정의
def bubble_sort_for_gns(arr):
    """
    전달받은 인자인 이중배열 리스트를 오름차순으로 정렬하는 함수
    하위 요소중 고정된 위치의 요소들로만 비교해서 정렬
    """
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j][1] > arr[j+1][1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


T = int(input())

for tc in range(1, T+1):
    '''
    "ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"
    위의 단어를 0 ~ 9에 대응하여 작은 수부터 차례로 정렬하여 출력하는 프로그램
    '''
    line = input().split()
    length = int(line[1])
    numbers = list(map(str, input().split()))
    another_numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    idx = 0
    for number in numbers:
        num = 0
        for another in another_numbers:
            if another == number:
                numbers[idx] = [number] + [num] + [idx]
            num += 1
        idx += 1

    sorted_numbers = bubble_sort_for_gns(numbers)
    result = [fin[0] for fin in sorted_numbers]

    print(f"#{tc} {' '.join(map(str, result))}")