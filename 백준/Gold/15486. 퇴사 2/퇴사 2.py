import sys

line = sys.stdin.readline

N = int(line())
schedule = [[]] + [list(map(int, line().split())) for _ in range(N)]
dp = [0] * (N + 2)
max_profit = 0
for i in range(1, N + 1):
    Ti = schedule[i][0]
    Pi = schedule[i][1]

    dp[i] = max(dp[i], dp[i-1])

    if i + Ti - 1 <= N:
        dp[i + Ti] = max(dp[i + Ti], dp[i] + Pi)

print(max(dp))
