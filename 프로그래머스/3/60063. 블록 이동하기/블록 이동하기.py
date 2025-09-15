from collections import deque

# 델타 (상하좌우 우상, 우하, 좌하, 좌상) (0 ~ 7)
delta = {0: (-1, 0), 1: (1, 0), 2: (0, -1), 3: (0, 1),
         4: (-1, 1), 5: (1, 1), 6: (1, -1), 7: (-1, -1)
         }

change_delta = {0: 1, 1: 0, 2: 3, 3: 2}


def solution(board):
    N = len(board)

    # 범위 및 벽 체크
    def free(r, c):
        return (0 <= r < N and 0 <= c < N) and board[r][c] == 0

    # 두 칸 정규화 상태
    def normalize(a, b):
        return tuple(sorted([a, b]))

    # 처음 상태
    start = normalize((0, 0), (0, 1))

    # 방문 처리
    visited = set([start])

    q = deque()
    # 로봇위치 1, 로봇위치 2, 시간
    q.append((start[0], start[1], 0))

    while q:
        (r1, c1), (r2, c2), t = q.popleft()

        # 종료조건
        # 두 칸 중 하나가 N - 1, N - 1 좌표 도착시
        if (r1, c1) == (N-1, N-1) or (r2, c2) == (N-1, N-1):
            return t

        # 이동 (회전 x)
        for i in range(4):
            nr1, nc1 = r1 + delta[i][0], c1 + delta[i][1]
            nr2, nc2 = r2 + delta[i][0], c2 + delta[i][1]

            if free(nr1, nc1) and free(nr2, nc2):
                nxt = normalize((nr1, nc1), (nr2, nc2))
                if nxt not in visited:
                    visited.add(nxt)
                    q.append(((nr1, nc1), (nr2, nc2), t+1))

        # 현재 로봇의 모양
        horizon = (r1 == r2)
        vertical = (c1 == c2)

        # 이동 (회전 o)
        # 1. 수평일 때: 위/아래 회전
        if horizon:
            for d_row in [-1, 1]:
                # 두 칸 위 또는 아래가 비어있어야 회전 가능
                if free(r1 + d_row, c1) and free(r2 + d_row, c2):
                    # 왼쪽 오른쪽을 축으로 회전
                    # 1. (r1, c1) 을 축으로
                    nxt1 = normalize((r1, c1), (r1 + d_row, c1))
                    if nxt1 not in visited:
                        visited.add(nxt1)
                        q.append(((r1, c1), (r1 + d_row, c1), t + 1))
                    # 2. (r2, c2)을 축으로
                    nxt2 = normalize((r2, c2), (r2 + d_row, c2))
                    if nxt2 not in visited:
                        visited.add(nxt2)
                        q.append(((r2, c2), (r2 + d_row, c2), t + 1))

        # 2. 수직일 때: 왼쪽 / 오른쪽 회전
        if vertical:
            for d_col in [-1, 1]:
                # 두 칸 좌/우가 모두 비어 있어야 회전 가능
                if free(r1, c1 + d_col) and free(r2, c2 + d_col):
                    # 위를 축으로 회전
                    # 1. (r1, c1) 을 축으로
                    nxt1 = normalize((r1, c1), (r1, c1 + d_col))
                    if nxt1 not in visited:
                        visited.add(nxt1)
                        q.append(((r1, c1), (r1, c1 + d_col), t + 1))
                    # 아래를 축으로 회전
                    # 2. (r2, c2)을 축으로
                    nxt2 = normalize((r2, c2), (r2, c2 + d_col))
                    if nxt2 not in visited:
                        visited.add(nxt2)
                        q.append(((r2, c2), (r2, c2 + d_col), t + 1))