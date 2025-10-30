import sys

line = sys.stdin.readline

# 델타 정의 (우좌상하)
drc = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}

# 주사위 상단 이동
dice = [0, 0, 0, 0, 0, 0]   # top, bottom, 북, 남, 동, 서


def roll(direction):
    t, b, n, s, e, w = dice

    if direction == 1:
        dice[0], dice[1], dice[4], dice[5] = w, e, t, b

    elif direction == 2:
        dice[0], dice[1], dice[4], dice[5] = e, w, b, t

    elif direction == 3:
        dice[0], dice[1], dice[2], dice[3] = s, n, t, b

    elif direction == 4:
        dice[0], dice[1], dice[2], dice[3] = n, s, b, t

    return dice


# 주사위 반대면
opposite = {0: 5, 1: 4, 2: 3, 3: 2, 4: 1, 5: 0}

N, M, r, c, K = map(int, line().split())
grid = [list(map(int, line().split())) for _ in range(N)]
command = list(map(int, line().split()))

top = 0
bottom = opposite[top]

for i in range(K):
    cur_command = command[i]
    dr, dc = drc[cur_command][0], drc[cur_command][1]

    nr, nc = r + dr, c + dc
    if 0 > nr or N <= nr or 0 > nc or M <= nc:
        continue

    r, c = nr, nc

    roll(cur_command)

    print(dice[0])

    if grid[nr][nc] == 0:
        grid[nr][nc] = dice[1]
    else:
        dice[1] = grid[nr][nc]
        grid[nr][nc] = 0


