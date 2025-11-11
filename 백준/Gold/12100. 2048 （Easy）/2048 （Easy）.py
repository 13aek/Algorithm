import sys
from collections import deque

line = sys.stdin.readline


def move(direction, b):
    """
    보드에서 입력된 방향으로 이동시 변경되는 보드를 반환하는 함수
    1, 2, 3, 4 = 상, 하, 좌, 우
    """
    b = [row[:] for row in b]
    if direction == 1:
        for c in range(N):
            q = deque()
            for r in range(N):
                if b[r][c] == 0:
                    continue

                if q:
                    if q[-1][0] == b[r][c] and not q[-1][1]:
                        comb = q.pop()[0] + b[r][c]
                        q.append((comb, True))
                        continue
                q.append((b[r][c], False))

            for r in range(N):
                if q:
                    num, _ = q.popleft()
                    b[r][c] = num
                else:
                    b[r][c] = 0
    elif direction == 2:
        for c in range(N):
            q = deque()
            for r in range(N - 1, -1, -1):
                if b[r][c] == 0:
                    continue

                if q:
                    if q[-1][0] == b[r][c] and not q[-1][1]:
                        comb = q.pop()[0] + b[r][c]
                        q.append((comb, True))
                        continue
                q.append((b[r][c], False))

            for r in range(N - 1, -1, -1):
                if q:
                    num, _ = q.popleft()
                    b[r][c] = num
                else:
                    b[r][c] = 0
    elif direction == 3:
        for r in range(N):
            q = deque()
            for c in range(N):
                if b[r][c] == 0:
                    continue

                if q:
                    if q[-1][0] == b[r][c] and not q[-1][1]:
                        comb = q.pop()[0] + b[r][c]
                        q.append((comb, True))
                        continue
                q.append((b[r][c], False))

            for c in range(N):
                if q:
                    num, _ = q.popleft()
                    b[r][c] = num
                else:
                    b[r][c] = 0
    elif direction == 4:
        for r in range(N):
            q = deque()
            for c in range(N - 1, -1, -1):
                if b[r][c] == 0:
                    continue

                if q:
                    if q[-1][0] == b[r][c] and not q[-1][1]:
                        comb = q.pop()[0] + b[r][c]
                        q.append((comb, True))
                        continue
                q.append((b[r][c], False))

            for c in range(N - 1, -1, -1):
                if q:
                    num, _ = q.popleft()
                    b[r][c] = num
                else:
                    b[r][c] = 0
    return b


def backtrack(m, previous_board, current_board):
    """
    상하좌우 방향으로 backtracking 하면서 5번 움직였을때 가장 큰 값을 반환하는 함수
    """
    global answer
    # 조기 종료 조건
    # 1. 이동한 블록의 모양이 이전 블록과 동일하다면
    if previous_board == current_board and m != 0:
        return

    # 2. 이동시킬 블록의 수가 하나밖에 남지 않았다면
    if sum(c.count(0) for c in current_board) == N * N - 1:
        score = max(map(max, current_board))
        if score > answer:
            answer = score
        return

    # 종료조건
    # m = 5 일 때, 이동 횟수가 5번이 되었을 때
    if m == 5:
        score = 0
        for lst in current_board:
            score = max(score, max(lst))
        if score > answer:
            answer = score
        return

    for i in range(1, 5):
        next_board = move(i, current_board)
        backtrack(m + 1, current_board, next_board)


N = int(line())
board = [list(map(int, line().split())) for _ in range(N)]
p_board = [row[:] for row in board]
answer = 0
for l in board:
    answer = max(answer, max(l))
backtrack(0, p_board, board)
print(answer)