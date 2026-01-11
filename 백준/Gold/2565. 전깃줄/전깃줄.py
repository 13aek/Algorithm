# BOJ Gold 5 2565_전깃줄 (LIS 응용 문제)

import sys

input = sys.stdin.readline

n = int(input())

lines = [tuple(map(int, input().split())) for _ in range(n)]

lines.sort()
a = [line[1] for line in lines]
dp = [1] * n

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))