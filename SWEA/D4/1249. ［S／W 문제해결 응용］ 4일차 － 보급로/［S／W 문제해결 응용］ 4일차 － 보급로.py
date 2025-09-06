# 델타 방향 정의 (우하좌상)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def dfs(info, row, col, current_recovery_time, visited):
    global min_recovery_time
    # 조기 종료 조건
    # 1. 도착지점에 도착했을때
    if row == N - 1 and col == N-1:
        if current_recovery_time < min_recovery_time:
            min_recovery_time = current_recovery_time
        return

    # 2. 복구 시간이 현재 최저 복구 시간보다 크면
    if current_recovery_time > min_recovery_time:
        return

    current_recovery_time += info[row][col]
    visited[row][col] = current_recovery_time

    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]

        if 0 <= nr < N and 0 <= nc < N:
            if visited[nr][nc] > current_recovery_time:
                dfs(info, nr, nc, current_recovery_time, visited)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    map_info = [list(map(int, input())) for _ in range(N)]

    visited = [[float('inf')] * N for _ in range(N)]

    min_recovery_time = sum(map_info[0]) + sum(row[N-1] for row in map_info[1:N])

    dfs(map_info, 0, 0, 0, visited)

    print(f"#{tc} {min_recovery_time}")