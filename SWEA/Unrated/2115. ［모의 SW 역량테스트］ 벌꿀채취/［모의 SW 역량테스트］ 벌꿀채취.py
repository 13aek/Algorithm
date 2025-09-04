from itertools import combinations

# 채취할 수 있는 벌꿀 찾기
def find_honey(arr):
    profit_list = []

    for r in range(N):
        for c in range(N - M + 1):
            for i in range(1, M + 1):
                profit = 0
                for comb in combinations(arr[r][c:c + M], i):
                    if C - sum(comb) < 0:
                        continue
                    else:
                        current_profit = 0
                        for com in comb:
                            current_profit += com**2
                        profit = max(profit, current_profit)

                profit_list += [[r, list(range(c, c+M)), profit]]

    profit_list.sort(key=lambda x: x[2], reverse=True)

    return profit_list


def calc_max(arr, visit):
    cnt = 0
    max_profit = 0
    for comb in combinations(list(range(len(arr))), 2):
        i, j = comb[0], comb[1]
        intersection = list(set(arr[i][1]) & set(arr[j][1]))
        if arr[i][0] == arr[j][0]:
            if not intersection:
                max_profit = max(max_profit, arr[i][2] + arr[j][2])
        else:
            max_profit = max(max_profit, arr[i][2] + arr[j][2])

    return max_profit


T = int(input())

for tc in range(1, T+1):
    # N: 벌통의 크기, M: 선택할 수 있는 벌통의 개수, C: 최대 양
    N, M, C = map(int, input().split())
    honeys = [list(map(int, input().split())) for _ in range(N)]

    visited = [[False] * N for _ in range(N)]

    p_list = find_honey(honeys)
    result = calc_max(p_list, visited)

    print(f"#{tc} {result}")