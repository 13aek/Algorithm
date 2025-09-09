from collections import deque

# 델타 방향 정의 (상, 우상, 우, 우하, 하, 좌하, 좌, 좌상)
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]


def bfs(start_row, start_col, arr):
    q = deque()
    q.append((start_row, start_col))
    visited = set()
    while q:
        cnt = 0
        candidates = []
        x, y = q.popleft()

        if (x, y) in visited:
            continue
        else:
            visited.add((x, y))

        for i in range(8):
            nr = x + dr[i]
            nc = y + dc[i]

            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] == '*':
                    cnt = 1
                    break
                elif arr[nr][nc] == '.':
                    candidates.append((nr, nc))

        if cnt == 0:
            for a, b in candidates:
                if (a, b) not in visited:
                    q.append((a, b))

    return len(visited), visited


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    string = [list(map(str, input().strip())) for _ in range(N)]
    seen = [[0] * N for _ in range(N)]
    result = 1

    click_candidates = []
    for r in range(N):
        for c in range(N):
            if string[r][c] != '*':
                is_star = False
                for i in range(8):
                    nr = r + dr[i]
                    nc = c + dc[i]

                    if 0 <= nr < N and 0 <= nc < N:
                        if string[nr][nc] == '*':
                            is_star = True
                            break
                if is_star:
                    click_candidates.append((1, r, c, [(r, c)]))
                else:
                    count, visit = bfs(r, c, string)
                    click_candidates.append((count, r, c, visit))

    click_candidates.sort(reverse=True, key=lambda x: x[0])

    is_clicked = set(click_candidates[0][3])
    for _, a, b, v in click_candidates[1:]:
        if (a, b) not in is_clicked:
            is_clicked |= set(v)
            result += 1

    print(f"#{tc} {result}")