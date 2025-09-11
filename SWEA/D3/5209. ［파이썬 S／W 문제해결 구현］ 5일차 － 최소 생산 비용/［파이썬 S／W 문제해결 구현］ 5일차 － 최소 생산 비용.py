def backtrack(arr, cur_r, cur_c, cur_cost):
    global min_cost

    n_cost = cur_cost + arr[cur_r][cur_c]

    # 종료 조건
    # 현재 행이 N 과 똑같아졌을때
    if cur_r == N - 1:
        if min_cost > n_cost:
            min_cost = n_cost
        return

    # 조기 종료 조건
    # 1. min_cost 보다 현재 cost 가 크거나 같을때
    if cur_cost >= min_cost:
        return
    # 2. 이미 기록된 col 일 경우
    if visited[cur_c]:
        return

    visited[cur_c] = True
    nr = cur_r + 1

    for nc in range(N):
        if not visited[nc]:
            backtrack(arr, nr, nc, n_cost)
            visited[nc] = False


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    Vij = [list(map(int, input().split())) for _ in range(N)]

    min_cost = float('inf')

    for c in range(N):
        visited = [False] * N
        backtrack(Vij, 0, c, 0)

    print(f"#{tc} {min_cost}")