import sys

line = sys.stdin.readline


def check(cur_row, cur_col, visited):
    changed = []
    for i in range(4):
        for k in range(1, N + 1):
            nr, nc = cur_row + dr[i] * k, cur_col + dc[i] * k

            if 0 > nr or N <= nr or nc < 0 or N <= nc:
                break

            if (nr, nc) in possible_place:
                idx = possible_place[(nr, nc)]
                if visited[idx]:
                    visited[idx] = False
                    changed.append(idx)
    return changed


def dfs(idx, cur_cnt, true_cnt, visit, pos_list, color):
    global black_ans, white_ans

    if color == 0:
        if (cur_cnt + true_cnt) <= black_ans:
            return
    else:
        if (cur_cnt + true_cnt) <= white_ans:
            return

    if color == 0:
        if idx == len(black):
            black_ans = max(black_ans, cur_cnt)
            return
    else:
        if idx == len(white):
            white_ans = max(white_ans, cur_cnt)
            return

    dfs(idx + 1, cur_cnt, true_cnt, visit, pos_list, color)

    cur_row, cur_col = pos_list[idx]
    position = possible_place[(cur_row, cur_col)]
    if visit[position]:
        visit[position] = False
        changed = [position] + check(cur_row, cur_col, visit)
        new_true_cnt = true_cnt - len(changed)
        dfs(idx + 1, cur_cnt + 1, new_true_cnt, visit, pos_list, color)
        for x in changed:
            visit[x] = True


# 델타 방향 정의 (우상, 우하, 좌하, 좌상)
dr = [-1, 1, 1, -1]
dc = [1, 1, -1, -1]

N = int(line())

b = 0
w = 0
possible_place = {}
black = []
white = []
for r in range(N):
    chess = list(map(int, input().split()))
    for c in range(N):
        if chess[c] == 1:
            if (r + c) % 2 == 0:
                possible_place[(r, c)] = b
                black.append((r, c))
                b += 1
            else:
                possible_place[(r, c)] = w
                white.append((r, c))
                w += 1

black_ans = 0
white_ans = 0
visited_black = [True] * len(black)
visited_white = [True] * len(white)
dfs(0, 0, len(black), visited_black, black, 0)
dfs(0, 0, len(white), visited_white, white, 1)

ans = black_ans + white_ans
print(ans)