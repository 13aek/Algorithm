import itertools

T = int(input())

for tc in range(1, T+1):
    N = int(input())    # 식재료의 수
    sij = [list(map(int, input().split())) for _ in range(N)]

    visited = [[False] * N for _ in range(N)]

    food_list = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if sij[r][c] + sij[c][r] != 0 and visited[r][c] is False:
                food_list[r][c] = sij[r][c] + sij[c][r]
                visited[r][c], visited[c][r] = True, True

    min_diff = float("inf")

    for group1 in itertools.combinations(list(range(N)), N//2):
        group2 = tuple(x for x in range(N) if x not in group1)

        a_food = 0
        for g1 in itertools.combinations(group1, 2):
            a_food += food_list[g1[0]][g1[1]]

        b_food = 0
        for g2 in itertools.combinations(group2, 2):
            b_food += food_list[g2[0]][g2[1]]

        min_diff = min(min_diff, abs(a_food - b_food))
        if min_diff == 0:
            break

    print(f"#{tc} {min_diff}")