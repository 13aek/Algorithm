# BOJ silver 2 11053_가장 긴 증가하는 부분 수열 (LIS)

import sys

line = sys.stdin.readline

N = int(line())
Ai = list(map(int, line().split()))

dp = [1] * N

for i in range(N):
    for j in range(i):
        if Ai[j] < Ai[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))