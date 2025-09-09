from collections import deque


def bfs(start_row, start_col):
    global cnt
    q = deque()
    q.append((start_row, start_col, 1))

    while q:
        r, c, s = q.popleft()

        if visited[r][c]:
            continue

        visited[r][c] = True
        cnt += 1

        for dr, dc in delta[tunnel[r][c]]:
            nr = r + dr
            nc = c + dc

            if (0 <= nr < N and 0 <= nc < M) and tunnel[nr][nc] != 0:
                if not visited[nr][nc]:
                    if is_possible(dr, dc, nr, nc):
                        if s + 1 <= L:
                            q.append((nr, nc, s + 1))


def is_possible(delta_row, delta_col, check_row, check_col):
    pos = True
    if (delta_row, delta_col) == (-1, 0):               # 상
        if tunnel[check_row][check_col] in [3, 4, 7]:
            pos = False
    elif (delta_row, delta_col) == (1, 0):              # 하
        if tunnel[check_row][check_col] in [3, 5, 6]:
            pos = False
    elif (delta_row, delta_col) == (0, -1):             # 좌
        if tunnel[check_row][check_col] in [2, 6, 7]:
            pos = False
    elif (delta_row, delta_col) == (0, 1):              # 우
        if tunnel[check_row][check_col] in [2, 4, 5]:
            pos = False

    return pos


T = int(input())

for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    cnt = 0
    # 지하 터널 델타 방향
    delta = [
        [],
        [(-1, 0), (1, 0), (0, -1), (0, 1)],
        [(-1, 0), (1, 0)],
        [(0, -1), (0, 1)],
        [(-1, 0), (0, 1)],
        [(1, 0), (0, 1)],
        [(1, 0), (0, -1)],
        [(-1, 0), (0, -1)],
    ]

    bfs(R, C)

    print(f"#{tc} {cnt}")