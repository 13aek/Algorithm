# BOJ Gold 4 11054_가장 긴 바이토닉 부분 수열 (LIS 응용 문제)

import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

dp = [1] * n
dp_reverse = [0] * n

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j] + 1)

for i in range(n - 1, -1, -1):
    for k in range(n - 1, i, -1):
        if a[i] > a[k]:
            dp_reverse[i] = max(dp_reverse[i], dp_reverse[k] + 1)

result = [x + y for x, y in zip(dp, dp_reverse)]

print(max(result))