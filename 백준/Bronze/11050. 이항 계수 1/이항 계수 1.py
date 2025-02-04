import math

N, K = map(int, input().split())

result = math.comb(N, K)

print(result)