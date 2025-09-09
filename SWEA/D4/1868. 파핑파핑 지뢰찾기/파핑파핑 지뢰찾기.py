from collections import deque

# 델타 방향 정의 (상, 우상, 우, 우하, 하, 좌하, 좌, 좌상)
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]


def bfs(start_row, start_col):
    q = deque()
    q.append((start_row, start_col))
    while q:
        x, y = q.popleft()

        if adj[x][y] == 0:
            for i in range(8):
                nr = x + dr[i]
                nc = y + dc[i]

                if 0 <= nr < N and 0 <= nc < N:
                    if adj[nr][nc] != -1 and not visited[nr][nc]:
                        visited[nr][nc] = True
                        if adj[nr][nc] == 0:
                            q.append((nr, nc))


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    string = [list(map(str, input().strip())) for _ in range(N)]
    result = 0

    adj = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if string[r][c] == '*':
                adj[r][c] = -1
                continue

            cnt = 0
            for i in range(8):
                nr = r + dr[i]
                nc = c + dc[i]

                if 0 <= nr < N and 0 <= nc < N:
                    if string[nr][nc] == '*':
                        cnt += 1
            adj[r][c] = cnt

    visited = [[False] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if adj[r][c] == 0 and not visited[r][c]:
                result += 1
                visited[r][c] = True
                bfs(r, c)

    for r in range(N):
        for c in range(N):
            if adj[r][c] >= 0 and not visited[r][c]:
                result += 1

    print(f"#{tc} {result}")

