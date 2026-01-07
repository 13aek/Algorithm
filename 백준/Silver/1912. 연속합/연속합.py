# BOJ silver 2 1912_연속합

import sys

line = sys.stdin.readline

n = int(line())
numbers = list(map(int, line().split()))

dp = [0] * n
dp[0] = numbers[0]

for i in range(1, n):
    dp[i] = max(numbers[i], dp[i-1] + numbers[i])

print(max(dp))