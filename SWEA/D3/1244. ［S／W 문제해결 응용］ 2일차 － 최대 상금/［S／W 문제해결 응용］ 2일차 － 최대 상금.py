def dfs(lst, k):
    global ans
    # 종료조건
    # 1. 교환 횟수를 모두 사용하였을 때
    if k == change:
        ans = max(ans, int("".join(lst)))
        return

    # 이미 체크했던 상태이면 (문자열, k)
    if (tuple(lst), k) in check:
        return

    check.add((tuple(lst), k))

    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n):
            lst[i], lst[j] = lst[j], lst[i]
            dfs(lst, k + 1)
            lst[i], lst[j] = lst[j], lst[i]


for tc in range(1, int(input()) + 1):
    input_num, input_change = input().split()

    numbers = list(input_num)
    change = int(input_change)

    ans = 0
    check = set()

    dfs(numbers, 0)

    print(f"#{tc} {ans}")