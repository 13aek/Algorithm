import math

N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

result = sum(math.ceil(size / T) for size in sizes)

pen_bundle = N // P
pen_remainder = N % P

print(result)
print(pen_bundle, pen_remainder)