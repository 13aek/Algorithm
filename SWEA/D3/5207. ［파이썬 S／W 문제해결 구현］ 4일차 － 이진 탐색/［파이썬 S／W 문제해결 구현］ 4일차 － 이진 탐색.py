def binary_search(arr, left, right, target, check):
    global cnt

    if left > right:
        return

    mid = (left + right) // 2

    if arr[mid] == target:
        cnt += 1
        return

    elif arr[mid] > target:
        if check == 1:
            return
        binary_search(arr, left, mid - 1, target, 1)

    else:
        if check == 2:
            return
        binary_search(arr, mid + 1, right, target, 2)


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))

    cnt = 0
    for t in B:
        binary_search(A, 0, N - 1, t, 0)

    print(f"#{tc} {cnt}")