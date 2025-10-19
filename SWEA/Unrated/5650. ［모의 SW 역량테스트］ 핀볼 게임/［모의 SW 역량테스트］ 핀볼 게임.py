from collections import deque

# 델타 방향 정의 (상하좌우 우하 좌상 좌하 우상)
drc = {0: (-1, 0), 1: (1, 0), 2: (0, -1), 3: (0, 1)}

# 블록별 방향 정의
block = {
    1: [1, 3, 0, 2],
    2: [3, 0, 1, 2],
    3: [2, 0, 3, 1],
    4: [1, 2, 3, 0],
    5: [1, 0, 3, 2],
}

# 벽 만날시 반대방향 정의
opposite = {0: 1, 1: 0, 2: 3, 3: 2}


def simulate(sr, sc, sd):
    cr, cc, d, s = sr, sc, sd, 0
    start = False

    while True:
        nr, nc = cr + drc[d][0], cc + drc[d][1]

        if 0 > nr or nr >= N or 0 > nc or nc >= N:
            return s * 2 + 1

        if (nr, nc) == (sr, sc) or pinball[nr][nc] == -1:
            return s

        if pinball[nr][nc] == 0:
            cr, cc, d, s = nr, nc, d, s
            continue

        elif 1 <= pinball[nr][nc] <= 4:
            block_num = pinball[nr][nc]
            change_dir = block[block_num][d]
            cr, cc, d, s = nr, nc, change_dir, s + 1
            continue

        elif pinball[nr][nc] == 5:
            return s * 2 + 1

        elif 6 <= pinball[nr][nc]:
            nr, nc = worm_hole[(nr, nc)]
            cr, cc, d, s = nr, nc, d, s
            continue


for tc in range(1, int(input()) + 1):
    N = int(input())
    pinball = [list(map(int, input().split())) for _ in range(N)]

    worm_hole_check = {}
    for r in range(N):
        for c in range(N):
            if 6 <= pinball[r][c] <= 10:
                worm_hole_check[pinball[r][c]] = worm_hole_check.get(pinball[r][c], []) + [(r, c)]

    worm_hole = {}
    for v in worm_hole_check.values():
        worm_hole[v[0]] = v[1]
        worm_hole[v[1]] = v[0]

    answer = 0
    for r in range(N):
        for c in range(N):
            if pinball[r][c] == 0:
                for i in range(4):
                    answer = max(answer, simulate(r, c, i))

    print(f"#{tc} {answer}")