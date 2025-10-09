import sys
from collections import deque

line = sys.stdin.readline

# 델타 방향 정의 (상하좌우)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(labor):
    q = deque(virus)
    safe = len(blank) - 3

    while q:
        cr, cc = q.popleft()

        for i in range(4):
            nr, nc = cr + dr[i], cc + dc[i]

            if (0 <= nr < N and 0 <= nc < M) and labor[nr][nc] == 0:
                labor[nr][nc] = 2
                q.append((nr, nc))
                safe -= 1
                if safe <= answer:
                    return 0

    return safe


def dfs(wall_count, start, visited, laboratory):
    global answer

    if wall_count == 3:
        lab = [row[:] for row in laboratory]
        count = bfs(lab)
        answer = max(answer, count)
        return

    for i in range(start, len(blank)):
        if not visited[i]:
            r, c = blank[i]
            visited[i] = True
            laboratory[r][c] = 1
            dfs(wall_count + 1, i + 1, visited, laboratory)
            laboratory[r][c] = 0
            visited[i] = False


N, M = map(int, line().split())
grid = [list(map(int, line().split())) for _ in range(N)]
virus = []
blank = []
for r in range(N):
    for c in range(M):
        if grid[r][c] == 2:
            virus.append((r, c))
        elif grid[r][c] == 0:
            blank.append((r, c))
answer = 0
visited = [False] * len(blank)
dfs(0, 0, visited, grid)
print(answer)