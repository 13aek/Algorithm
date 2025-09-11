# 델타 방향 (상하좌우)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(cur_r, cur_c, cur_num):
    global ans

    # 종료 조건
    # 1. cur_num 의 자리 수가 7개가 됐을 때
    if len(cur_num) == 7:
        ans.add(int(cur_num))
        return

    for i in range(4):
        nr, nc = cur_r + dr[i], cur_c + dc[i]

        if 0 <= nc < 4 and 0 <= nr < 4:
            next_num = cur_num + str(grid[nr][nc])
            dfs(nr, nc, next_num)


T = int(input())

for tc in range(1, T + 1):
    grid = [list(map(int, input().split())) for _ in range(4)]

    ans = set()

    for r in range(4):
        for c in range(4):
            dfs(r, c, str(grid[r][c]))

    print(f"#{tc} {len(ans)}")