from itertools import product
from collections import deque


# 델타 방향 정의 (상하좌우)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(cur_row, cur_col):
    # 현재 좌표 (cur_row, cur_col)에서 벽돌 깨뜨리는 BFS
    q = deque()
    q.append((cur_row, cur_col, brick_copy[cur_row][cur_col]))

    while q:
        x, y, s = q.popleft()

        if s == 1:      # 숫자가 1이면 자기 자신만 깨지고 종료
            brick_copy[x][y] = 0
            continue

        # 숫자가 2 이상이면, 상하좌우로 (s-1)칸 만큼 영향을 미침
        for k in range(1, brick_copy[x][y]):
            for i in range(4):
                nx = x + dr[i] * k
                ny = y + dc[i] * k

                # 격자 안에 있고, 벽돌이 존재하면 큐에 추가
                if (0 <= nx < H and 0 <= ny < W) and brick_copy[nx][ny] != 0:
                    q.append((nx, ny, brick_copy[nx][ny]))

        # 자기 자신은 0으로 만들기 (깨짐)
        brick_copy[x][y] = 0


def rearrange_array(arr):
    # 벽돌이 깨진 후, 중력 처리 (벽돌들이 아래로 내려옴)
    stack = []
    for c in range(W):
        for r in range(H):
            if arr[r][c] != 0:  # 벽돌이 있으면 stack 에 담고 원래 자리는 0
                stack.append(arr[r][c])
                arr[r][c] = 0

        # 밑에서부터 채워 넣기
        while stack:
            arr[r][c] = stack.pop()
            r -= 1

    return arr


T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    brick = [list(map(int, input().split())) for _ in range(H)]

    min_brick = float('inf')    # 최소 벽돌 개수 저장

    # product: W개의 열 중에서 N번 선택하는 모든 경우 (중복 + 순서 고려)
    for comb in product(range(W), repeat=N):
        brick_copy = [row[:] for row in brick]
        cur_brick = 0   # 현재 남은 벽돌 개수

        for p in comb:
            i = -1
            # 구슬이 떨어져 처음 맞는 벽돌 찾기 (맨 위에서부터)
            for r in range(H):
                if brick_copy[r][p] != 0:
                    i = r
                    break

            if i == -1:     # 해당 열에 벽돌이 없으면 아무 일도 안 일어남
                break

            bfs(i, p)                       # 벽돌 깨뜨리기
            rearrange_array(brick_copy)     # 중력 처리

        # 남아있는 벽돌 개수 세기
        for r in range(H):
            cur_brick += (W - brick_copy[r].count(0))

        # 최소값 갱신
        if cur_brick < min_brick:
            min_brick = cur_brick
        
        # 남은 벽돌이 0이면 조합 반복 중단
        if min_brick == 0:
            break

    print(f"#{tc} {min_brick}")