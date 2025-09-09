from itertools import product
from collections import deque

# 델타 방향 정의 (상하좌우)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(cur_row, cur_col):
    visited = [[False] * W for _ in range(H)]
    q = deque()
    q.append((cur_row, cur_col, brick_copy[cur_row][cur_col]))

    while q:
        x, y, s = q.popleft()

        if visited[x][y]:
            continue

        visited[x][y] = True

        if s == 1:
            brick_copy[x][y] = 0
            continue

        for k in range(1, brick_copy[x][y]):
            for i in range(4):
                nx = x + dr[i] * k
                ny = y + dc[i] * k

                if (0 <= nx < H and 0 <= ny < W) and brick_copy[nx][ny] != 0:
                    q.append((nx, ny, brick_copy[nx][ny]))

        brick_copy[x][y] = 0


def rearrange_array(arr):
    stack = []
    for c in range(W):
        for r in range(H):
            if arr[r][c] != 0:
                stack.append(arr[r][c])
                arr[r][c] = 0
        while stack:
            arr[r][c] = stack.pop()
            r -= 1

    return arr


T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    brick = [list(map(int, input().split())) for _ in range(H)]
    min_brick_arr = []
    min_brick = float('inf')
    for comb in product(range(W), repeat=N):
        brick_copy = [row[:] for row in brick]
        cur_brick = 0
        for p in comb:
            i = -1
            for r in range(H):
                if brick_copy[r][p] != 0:
                    i = r
                    break

            if i == -1:
                break

            bfs(i, p)
            rearrange_array(brick_copy)

        for r in range(H):
            cur_brick += (W - brick_copy[r].count(0))

        if cur_brick < min_brick:
            min_brick = cur_brick

    print(f"#{tc} {min_brick}")