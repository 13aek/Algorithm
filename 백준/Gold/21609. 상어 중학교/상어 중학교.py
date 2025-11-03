import sys
from collections import deque

line = sys.stdin.readline

# 델타 방향정의
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def distance(cur_row, cur_col, nxt_row, nxt_col):
    if abs(cur_row - nxt_row) + abs(cur_col - nxt_col) == 1:
        return True
    else:
        return False


def bfs(start_row, start_col):
    q = deque([(start_row, start_col)])
    visit = {(start_row, start_col)}
    cnt_2 = 1   # 현재 기준 블록에서의 점수
    block_num = blocks[start_row][start_col]
    rainbow_block = 0

    while q:
        cr, cc = q.popleft()

        for i in range(4):
            nr, nc = cr + dr[i], cc + dc[i]

            if 0 <= nr < N and 0 <= nc < N:
                if (nr, nc) not in visit:
                    if blocks[nr][nc] == block_num:
                        visited[nr][nc] = True
                        cnt_2 += 1
                        visit.add((nr, nc))
                        q.append((nr, nc))
                    elif blocks[nr][nc] == 0:
                        visited[nr][nc] = True
                        cnt_2 += 1
                        rainbow_block += 1
                        visit.add((nr, nc))
                        q.append((nr, nc))

    return cnt_2, rainbow_block, visit


def gravity(grid):
    for c in range(N):
        stack = []
        for r in range(N):
            if grid[r][c] >= 0:
                stack.append(grid[r][c])
                grid[r][c] = -2
            elif grid[r][c] == -1:
                cur_r = r
                while stack:
                    if grid[cur_r][c] == -2:
                        grid[cur_r][c] = stack.pop()
                        cur_r -= 1
                    else:
                        cur_r -= 1

        cur_r = N - 1

        while stack:
            if grid[cur_r][c] == -2:
                grid[cur_r][c] = stack.pop()
                cur_r -= 1
            else:
                cur_r -= 1

    return grid


N, M = map(int, line().split())
blocks = [list(map(int, line().split())) for _ in range(N)]

# 1. 크기가 가장 큰 블록 그룹 찾기 -> bfs
# 1.1 블록 그룹이 여러 개라면 포함된 무지개 블록의 수가 가장 많은 블록 그룹
# 1.2 기준 블록의 행이 가장 큰 것
# 1.3 열이 가장 큰 것
score = 0

while True:
    cnt_1 = 0   # 현재 block 에서 없어질 블록의 최고 개수
    rainbow = 0     # 현재 최고 블록에서의 무지개 블록
    candidate = set()   # 현재 최고 개수에서 없어질 블록
    std_row, std_column = -1, -1    # 현재 최고 개수에서의 기준 블록 위치
    visited = [[False] * N for _ in range(N)]   # 현재 블록에서의 탐색 여부

    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                visited[r][c] = True
                if blocks[r][c] > 0:
                    cur_cnt, cur_rainbow, cur_candi = bfs(r, c)

                    if cur_cnt <= 1:
                        continue

                    if cur_cnt > cnt_1:
                        cnt_1 = cur_cnt
                        rainbow = cur_rainbow
                        candidate = cur_candi
                        std_row, std_column = r, c

                    elif cur_cnt == cnt_1:
                        if rainbow < cur_rainbow:
                            cnt_1 = cur_cnt
                            rainbow = cur_rainbow
                            candidate = cur_candi
                            std_row, std_column = r, c
                        elif rainbow == cur_rainbow:
                            if std_row < r:
                                cnt_1 = cur_cnt
                                rainbow = cur_rainbow
                                candidate = cur_candi
                                std_row, std_column = r, c
                            elif std_row == r:
                                if std_column < c:
                                    cnt_1 = cur_cnt
                                    rainbow = cur_rainbow
                                    candidate = cur_candi
                                    std_row, std_column = r, c

    if cnt_1 < 2:
        break

    score += cnt_1 ** 2

    for (r, c) in candidate:
        blocks[r][c] = -2

    blocks = gravity(blocks)

    blocks = list(map(list, zip(*blocks)))[::-1]

    blocks = gravity(blocks)

print(score)
