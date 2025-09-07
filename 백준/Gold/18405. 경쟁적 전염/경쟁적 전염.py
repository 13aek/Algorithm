import sys
from collections import deque

# 델타 방향설정 (상하좌우)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(cur_r, cur_c):
    global test_tube, cur_visited

    q = deque()
    q.append((cur_r, cur_c))

    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if test_tube[nr][nc] == 0:
                    test_tube[nr][nc] = test_tube[r][c]
                    cur_visited[nr][nc] = True

                elif cur_visited[nr][nc] and test_tube[nr][nc] > test_tube[r][c]:
                    test_tube[nr][nc] = test_tube[r][c]


line = sys.stdin.readline
N, K = map(int, line().split())
test_tube = [list(map(int, line().split())) for _ in range(N)]
S, X, Y = map(int, line().split())

visited = [[False] * N for _ in range(N)]

for s in range(1, S + 1):
    if test_tube[X-1][Y-1] != 0:
        break
    cur_visited = [[False] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if test_tube[r][c] != 0 and not cur_visited[r][c] and not visited[r][c]:
                visited[r][c] = True
                bfs(r, c)
                
print(test_tube[X-1][Y-1])