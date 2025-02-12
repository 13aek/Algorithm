import sys

n, m = map(int, sys.stdin.readline().split())
board = [sys.stdin.readline().strip() for _ in range(n)]

chess1 = ['BWBWBWBW', 'WBWBWBWB'] * 4
chess2 = ['WBWBWBWB', 'BWBWBWBW'] * 4

min_repaint = float('inf')

for i in range(n - 7):
    for j in range(m - 7):
        repaint1, repaint2 = 0, 0

        for x in range(8):
            for y in range(8):
                if board[i + x][j + y] != chess1[x][y]:
                    repaint1 += 1
                if board[i + x][j + y] != chess2[x][y]:
                    repaint2 += 1

        min_repaint = min(min_repaint, repaint1, repaint2)

print(min_repaint)
