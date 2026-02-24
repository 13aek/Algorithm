# BOJ Gold 1 11003_최솟값_찾기

import sys
from collections import deque

input = sys.stdin.readline

N, L = map(int, input().split())

q = deque()

i = 0

for number in map(int, input().split()):
    i += 1
    
    while q and q[-1][0] > number:
        q.pop()

    q.append((number, i))

    if q[0][1] < i - L + 1:
        q.popleft()
    
    print(q[0][0], end=' ')