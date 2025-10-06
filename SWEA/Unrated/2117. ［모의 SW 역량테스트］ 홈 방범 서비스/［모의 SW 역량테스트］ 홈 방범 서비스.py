from collections import deque

# 델타 정의 (상하좌우)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def maintenance_cost(k):
    return k * k + (k - 1) * (k - 1)


def bfs(start_r, start_c, count):
    global result

    visited = [[False] * N for _ in range(N)]
    visited[start_r][start_c] = True
    q = deque([(start_r, start_c, 1)])
    k = 1
    h = count
    cost = h * M

    while q:
        cur_r, cur_c, cur_k = q.popleft()

        if cur_k != k:
            if cost - maintenance_cost(cur_k) >= 0:
                result = max(result, h)
            k = cur_k

        for i in range(4):
            nr, nc = cur_r + dr[i], cur_c + dc[i]

            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if city[nr][nc] == 1:
                    h += 1
                    cost += M
                visited[nr][nc] = True
                q.append((nr, nc, cur_k + 1))


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]

    result = 1

    for r in range(N):
        for c in range(N):
            cnt = 0
            if city[r][c] == 1:
                cnt = 1
            bfs(r, c, cnt)

    print(f"#{tc} {result}")