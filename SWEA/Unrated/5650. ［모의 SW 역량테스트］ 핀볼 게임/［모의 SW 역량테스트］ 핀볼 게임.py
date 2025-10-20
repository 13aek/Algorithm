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

    while True:
        # 다음 위치
        nr, nc = cr + drc[d][0], cc + drc[d][1]

        # 벽이나 5번 블럭을 만나면 리턴
        if 0 > nr or nr >= N or 0 > nc or nc >= N or pinball[nr][nc] == 5:
            return s * 2 + 1

        cell = pinball[nr][nc]

        # 시작 위치로 돌아오거나 블랙홀 만나면 리턴
        if (nr, nc) == (sr, sc) or cell == -1:
            return s

        # 다음위치가 빈 공간이면 다음 위치로 현재위치 업데이트
        if cell == 0:
            cr, cc, d, s = nr, nc, d, s
            continue

        # 1 ~ 4번 벽을 만나면 방향 바꾸고 현재 위치 업데이트
        elif 1 <= cell <= 4:
            block_num = pinball[nr][nc]
            change_dir = block[block_num][d]
            cr, cc, d, s = nr, nc, change_dir, s + 1
            continue

        # 웜홀 만나면 연결된 웜홀 위치로 현재 위치 업데이트
        elif 6 <= cell:
            x1, y1 = worm_hole[cell][0]
            x2, y2 = worm_hole[cell][1]
            if (nr, nc) == (x1, y1):
                cr, cc, d, s = x2, y2, d, s
            else:
                cr, cc, d, s = x1, y1, d, s
            continue


for tc in range(1, int(input()) + 1):
    N = int(input())
    pinball = [list(map(int, input().split())) for _ in range(N)]

    # 웜홀 위치 체크
    worm_hole = {}
    for r in range(N):
        for c in range(N):
            if 6 <= pinball[r][c] <= 10:
                worm_hole[pinball[r][c]] = worm_hole.get(pinball[r][c], []) + [(r, c)]

    answer = 0
    # pinball map 순회
    for r in range(N):
        for c in range(N):
            # 빈 공간일때
            if pinball[r][c] == 0:
                # 4방향으로 탐색
                for i in range(4):
                    answer = max(answer, simulate(r, c, i))

    print(f"#{tc} {answer}")