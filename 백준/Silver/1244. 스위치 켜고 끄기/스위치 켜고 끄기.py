import sys
from copy import deepcopy

N = int(sys.stdin.readline())
status = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
gender_button = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

status_copy = deepcopy(status)

for gb in gender_button:
    if N % 2 == 0:
        symmetric = N//2 - 1
    else:
        symmetric = N//2

    # 성별이 남자이면
    if gb[0] == 1:
        for i in range(len(status_copy)):
            if (i + 1) % gb[1] == 0:
                if status_copy[i] == 0:
                    status_copy[i] = 1
                else:
                    status_copy[i] = 0
    # 성별이 여자이면
    else:
        for i in range(len(status_copy)):
            if i + 1 == gb[1]:
                cnt = 0
                for j in range(1, symmetric + 1):
                    if i + j in list(range(N)) and i-j in list(range(N)):
                        if status_copy[i + j] == status_copy[i - j]:
                            cnt = j
                        else:
                            break
                for a in range(gb[1] - 1 - cnt, gb[1] + cnt):
                    if status_copy[a] == 0:
                        status_copy[a] = 1
                    else:
                        status_copy[a] = 0

for i in range(0, len(status_copy), 20):
    line = ' '.join(map(str, status_copy[i:i+20]))
    print(line)