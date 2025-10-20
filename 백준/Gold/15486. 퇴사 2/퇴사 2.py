import sys

line = sys.stdin.readline

N = int(line())
dp = [0] * (N + 1)

for i in range(1, N + 1):
    Ti, Pi = map(int, line().split())

    dp[i] = max(dp[i], dp[i-1])

    if i + Ti - 1 <= N:
        dp[i + Ti - 1] = max(dp[i + Ti - 1], dp[i - 1] + Pi)

print(dp[N])
