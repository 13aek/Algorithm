import sys

line = sys.stdin.readline

N = int(line())

dp_min = [0, 0, 0]
dp_max = [0, 0, 0]

top = 0
while top < N:
    ct = list(map(int, line().split()))
    cur_min = [0, 0, 0]
    cur_max = [0, 0, 0]

    for i in range(3):
        if i == 0:
            cur_min[i] = min(ct[i] + dp_min[i], ct[i] + dp_min[i + 1])
            cur_max[i] = max(ct[i] + dp_max[i], ct[i] + dp_max[i + 1])
        elif i == 1:
            cur_min[i] = min(ct[i] + dp_min[i], ct[i] + dp_min[i + 1], ct[i] + dp_min[i - 1])
            cur_max[i] = max(ct[i] + dp_max[i], ct[i] + dp_max[i + 1], ct[i] + dp_max[i - 1])
        else:
            cur_min[i] = min(ct[i] + dp_min[i], ct[i] + dp_min[i - 1])
            cur_max[i] = max(ct[i] + dp_max[i], ct[i] + dp_max[i - 1])

    dp_min = cur_min
    dp_max = cur_max
    top += 1

print(max(dp_max), min(dp_min))