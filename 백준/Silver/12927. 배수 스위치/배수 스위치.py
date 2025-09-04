import sys

bulb = list(sys.stdin.readline().strip())

cnt = 0
for i in range(len(bulb)):
    if bulb[i] == 'Y':
        for j in range(len(bulb)):
            if (j + 1) % (i + 1) == 0:
                if bulb[j] == 'Y':
                    bulb[j] = 'N'
                else:
                    bulb[j] = 'Y'
        cnt += 1

if 'Y' in bulb:
    cnt = -1

print(cnt)