import sys
from collections import deque
line = sys.stdin.readline


# 델타 방향 정의 (상하좌우)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(virus_place):
    visited = [[False] * N for _ in range(N)]
    check = M
    q = deque()
    for i in range(len(virus)):
        if virus_place[i]:
            r, c, t = virus[i]
            visited[r][c] = True
            q.append((r, c, t))

    while q:
        cr, cc, ct = q.popleft()

        if ct > answer:
            return float('inf')

        for i in range(4):
            nr, nc = cr + dr[i], cc + dc[i]

            if (0 <= nr < N and 0 <= nc < N) and laboratory[nr][nc] != 1:
                if not visited[nr][nc]:
                    visited[nr][nc] = True
                    check += 1
                    q.append((nr, nc, ct + 1))

    if check == blank:
        return ct
    else:
        return float('inf')


def dfs(virus_count, start, lab, visited_virus):
    global answer

    if virus_count == 0:
        time = bfs(visited_virus)
        answer = min(answer, time)
        return

    for i in range(start, len(virus)):
        if not visited_virus[i]:
            visited_virus[i] = True
            dfs(virus_count - 1, i + 1, lab, visited_virus)
            visited_virus[i] = False


N, M = map(int, line().split())
laboratory = [list(map(int, line().split())) for _ in range(N)]
virus = []
blank = 0
for r in range(N):
    for c in range(N):
        if laboratory[r][c] == 2:
            virus.append((r, c, 0))
            blank += 1
        elif laboratory[r][c] == 0:
            blank += 1

answer = float('inf')
visited_virus = [False] * len(virus)
dfs(M, 0, laboratory, visited_virus)

print(-1 if answer == float('inf') else answer)