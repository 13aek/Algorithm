import sys
from collections import deque

line = sys.stdin.readline

# 델타 방향 정의
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
dh = [-1, 1]


def simulate(tomato_box):
    day = 0
    cnt = ripe_tomato
    box = deque(tomato_box)

    while box:
        r, c, h, d = box.popleft()

        if d != day:
            day = d

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if (0 <= nr < N and 0 <= nc < M) and warehouse[h][nr][nc] == 0:
                box.append((nr, nc, h, d + 1))
                warehouse[h][nr][nc] = 1
                cnt += 1

        for j in range(2):
            nh = h + dh[j]

            if 0 <= nh < H:
                if warehouse[nh][r][c] == 0:
                    box.append((r, c, nh, d + 1))
                    warehouse[nh][r][c] = 1
                    cnt += 1

    return -1 if cnt != total_tomato else day


M, N, H = map(int, line().split())
warehouse = [
    [list(map(int, line().split())) for _ in range(N)]
    for _ in range(H)
]
tomato = []
ripe_tomato = 0
unripe_tomato = 0
for h in range(H):
    for r in range(N):
        for c in range(M):
            if warehouse[h][r][c] != -1:
                if warehouse[h][r][c] == 1:
                    tomato.append((r, c, h, 0))
                    ripe_tomato += 1
                elif warehouse[h][r][c] == 0:
                    unripe_tomato += 1

total_tomato = ripe_tomato + unripe_tomato

if not unripe_tomato:
    print(0)
else:
    result = simulate(tomato)
    print(result)