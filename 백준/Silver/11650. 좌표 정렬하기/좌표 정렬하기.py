import sys

n = int(input())
points = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

points.sort()

for x,y in points:
    print(x,y)