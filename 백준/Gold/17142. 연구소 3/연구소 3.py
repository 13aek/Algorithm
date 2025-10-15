import sys
from heapq import heappop, heappush

line = sys.stdin.readline

# 델타 방향 정의 (상하좌우)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(virus_place):
    visited = [[False] * N for _ in range(N)]
    check = 0
    pq = []
    for i in range(len(virus)):
        if virus_place[i]:
            r, c, t = virus[i]
            visited[r][c] = True
            heappush(pq, (t, r, c))
        else:
            r, c, _ = virus[i]
            visited[r][c] = '*'
    result = 0

    while pq:
        ct, cr, cc = heappop(pq)
        # ct, cr, cc = q.popleft()

        if result >= answer:
            return float('inf')

        for i in range(4):
            nr, nc = cr + dr[i], cc + dc[i]

            if (0 <= nr < N and 0 <= nc < N) and laboratory[nr][nc] != 1:
                if not visited[nr][nc]:
                    visited[nr][nc] = True
                    check += 1
                    heappush(pq, (ct + 1, nr, nc))
                    result = ct + 1
                elif visited[nr][nc] == '*':
                    visited[nr][nc] = True
                    heappush(pq, (ct + 1, nr, nc))

    if check == blank:
        return result
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
        elif laboratory[r][c] == 0:
            blank += 1

answer = float('inf')
visited_virus = [False] * len(virus)
dfs(M, 0, laboratory, visited_virus)

print(-1 if answer == float('inf') else answer)