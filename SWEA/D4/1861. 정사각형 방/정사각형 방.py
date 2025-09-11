from collections import deque

# 델타 정의 (상하좌우)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(cur_r, cur_c):
    global ans
    cur_move = -1
    q = deque()
    q.append((1, Aij[cur_r][cur_c], cur_r, cur_c))

    while q:
        cnt, num, r, c = q.popleft()

        if cnt >= cur_move:
            cur_move = cnt

        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]

            if 0 <= nr < N and 0 <= nc < N:
                if Aij[nr][nc] == num + 1:
                    q.append((cnt + 1, num + 1, nr, nc))

    if cur_move > ans[1]:
        ans[1] = cur_move
        ans[0] = Aij[cur_r][cur_c]

    elif cur_move == ans[1]:
        if ans[0] > Aij[cur_r][cur_c]:
            ans[0] = Aij[cur_r][cur_c]


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    Aij = [list(map(int, input().split())) for _ in range(N)]
    ans = [-1, -1]

    for r in range(N):
        for c in range(N):
            if N ** 2 - Aij[r][c] + 1 <= ans[1]:
                continue
            bfs(r, c)

    print(f"#{tc} {ans[0]} {ans[1]}")
