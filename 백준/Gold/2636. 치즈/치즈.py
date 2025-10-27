import sys
from collections import deque

# 델타 방향정의 (상하좌우)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs():
    q = deque()
    q.append((0, 0))   # 현재 시간, 현재 r, 현재 c, 공기 접촉 여부
    cheese = deque()
    visited = [[False] * M for _ in range(N)]
    time = 0
    cheese_cnt = 0

    while q:
        cr, cc = q.popleft()

        if visited[cr][cc]:
            continue

        visited[cr][cc] = True

        for i in range(4):
            nr, nc = cr + dr[i], cc + dc[i]

            if (0 <= nr < N and 0 <= nc < M) and not visited[nr][nc]:
                if square[nr][nc] == 0:
                    q.append((nr, nc))
                else:
                    visited[nr][nc] = True
                    cheese.append((0, nr, nc))

    while cheese:
        t, row, col = cheese.popleft()

        if t != time:
            time = t
            cheese_cnt = 0

        cheese_cnt += 1

        for i in range(4):
            n_row, n_col = row + dr[i], col + dc[i]

            if (0 <= n_row < N and 0 <= n_col < M) and not visited[n_row][n_col]:
                if square[n_row][n_col] == 0:
                    hole = deque([(n_row, n_col)])
                    visited[n_row][n_col] = True

                    while hole:
                        r, c = hole.popleft()

                        for i in range(4):
                            nr, nc = r + dr[i], c + dc[i]

                            if (0 <= nr < N and 0 <= nc < M) and not visited[nr][nc]:
                                if square[nr][nc] == 0:
                                    visited[nr][nc] = True
                                    hole.append((nr, nc))
                                else:
                                    visited[nr][nc] = True
                                    cheese.append((t + 1, nr, nc))
                else:
                    visited[n_row][n_col] = True
                    cheese.append((t + 1, n_row, n_col))

    return time + 1, cheese_cnt


line = sys.stdin.readline

N, M = map(int, line().split())
square = [list(map(int, line().split())) for _ in range(N)]

result = bfs()
print(result[0])
print(result[1])
