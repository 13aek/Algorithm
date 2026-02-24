import sys
from collections import deque

input = sys.stdin.readline
write = sys.stdout.write

N, L = map(int, input().split())
arr = list(map(int, input().split()))

dq = deque()
result = []

for i in range(N):
    
    # 현재 값보다 큰 값은 제거
    while dq and arr[dq[-1]] > arr[i]:
        dq.pop()
    
    dq.append(i)  # 인덱스만 저장
    
    # 범위 벗어난 인덱스 제거
    if dq[0] < i - L + 1:
        dq.popleft()
    
    result.append(str(arr[dq[0]]))

write(" ".join(result))