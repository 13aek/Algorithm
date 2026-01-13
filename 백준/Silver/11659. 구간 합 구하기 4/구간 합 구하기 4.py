# BOJ Silver 3 구간 합 구하기 4

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

numbers = list(map(int, input().split()))

prefix_sum = [0] * (n + 1)

for i in range(1, n + 1):
    prefix_sum[i] = numbers[i - 1] + prefix_sum[i - 1]

for _ in range(m):
    x1, x2 = map(int, input().split())
    print(prefix_sum[x2] - prefix_sum[x1 - 1])