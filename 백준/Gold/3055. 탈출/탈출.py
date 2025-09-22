import sys
from heapq import heappush, heappop, heapify

# 델타 정의 (상 하 좌 우)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(info):
    pq = info
    heapify(pq)

    while pq:
        cur_t, r, c, category = heappop(pq)

        if category == '*':
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]

                if 0 <= nr < R and 0 <= nc < C:
                    if not grid[nr][nc]:
                        grid[nr][nc] = '*'
                        heappush(pq, (cur_t + 1, nr, nc, '*'))
                    elif grid[nr][nc] == 'S':
                        grid[nr][nc] = '*'
                        heappush(pq, (cur_t + 1, nr, nc, '*'))
        else:
            if (r, c) == destination:
                return cur_t

            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < R and 0 <= nc < C:
                    if not grid[nr][nc] or forest[nr][nc] == 'D':
                        grid[nr][nc] = 'S'
                        heappush(pq, (cur_t + 1, nr, nc, 'S'))
    return 'KAKTUS'


line = sys.stdin.readline

R, C = map(int, line().split())
forest = [list(line().strip()) for _ in range(R)]

grid = [[''] * C for _ in range(R)]
destination = ()
place = []

for r in range(R):
    for c in range(C):
        if forest[r][c] == '.':
            continue
        elif forest[r][c] == 'D':
            destination = (r, c)
            grid[r][c] = 'D'
        elif forest[r][c] == 'X':
            grid[r][c] = 'X'
        elif forest[r][c] == 'S':
            place.append((0, r, c, 'S'))
        elif forest[r][c] == '*':
            place.append((0, r, c, '*'))
            grid[r][c] = '*'

ans = bfs(place)
print(ans)