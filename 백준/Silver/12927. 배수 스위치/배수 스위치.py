import sys

bulb = list(sys.stdin.readline().strip())

cnt = 0
for i in range(len(bulb)):
    # 현재 전구가 켜져 있으면
    if bulb[i] == 'Y':
        # 현재 위치부터 배수를 돌면서 전구의 상태를 반전시킴
        for j in range(i, len(bulb)):
            if (j + 1) % (i + 1) == 0:
                if bulb[j] == 'Y':
                    bulb[j] = 'N'
                else:
                    bulb[j] = 'Y'
        # 횟수 + 1
        cnt += 1

# 전구의 상태가 켜진게 있으면
if 'Y' in bulb:
    # -1
    cnt = -1

print(cnt)