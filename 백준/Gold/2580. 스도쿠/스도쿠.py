import sys

line = sys.stdin.readline

board = [list(map(int, line().split())) for _ in range(9)]

blanks = []
for r in range(9):
    for c in range(9):
        if board[r][c] == 0:
            blanks.append((r, c))


def is_valid(r, c, num):
    for i in range(9):
        if board[r][i] == num or board[i][c] == num:
            return False

    nr, nc = (r // 3) * 3, (c // 3) * 3
    for i in range(nr, nr + 3):
        for j in range(nc, nc + 3):
            if board[i][j] == num:
                return False
            
    return True


def dfs(idx):
    # 종료 조건
    # 모든 빈칸이 채워질 때
    if idx == len(blanks):
        for row in board:
            print(*row)
        sys.exit(0)

    r, c = blanks[idx]
    for num in range(1, 10):
        if is_valid(r, c, num):
            board[r][c] = num
            dfs(idx + 1)
            board[r][c] = 0


dfs(0)