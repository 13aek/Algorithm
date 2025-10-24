import sys

line = sys.stdin.readline

N = int(line())
Ai = list(map(int, line().split()))
add, sub, mul, div = map(int, line().split())

# 결과 초기화
max_value = -float('inf')
min_value = float('inf')


def dfs(idx, cur, add, sub, mul, div):
    global max_value, min_value

    # 모든 수를 사용했을 때 결과 갱신
    if idx == N:
        max_value = max(max_value, cur)
        min_value = min(min_value, cur)
        return

    # 덧셈 사용 가능하면
    if add > 0:
        dfs(idx + 1, cur + Ai[idx], add - 1, sub, mul, div)

    # 뺄셈 사용 가능하면
    if sub > 0:
        dfs(idx + 1, cur - Ai[idx], add, sub - 1, mul, div)

    # 곱셈 사용 가능하면
    if mul > 0:
        dfs(idx + 1, cur * Ai[idx], add, sub, mul - 1, div)

    # 나눗셈 사용 가능하면
    if div > 0:
        if cur < 0:
            dfs(idx + 1, -(-cur // Ai[idx]), add, sub, mul, div - 1)
        else:
            dfs(idx + 1, cur // Ai[idx], add, sub, mul, div - 1)


# DFS 시작 (첫 번째 수부터 시작)
dfs(1, Ai[0], add, sub, mul, div)

# 결과 출력
print(max_value)
print(min_value)