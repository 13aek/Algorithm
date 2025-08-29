def dfs(r, c):
    # 종료 조건
    if maze[r][c] == 3:
        return 1

    # 현재 위치 방문 처리
    visited[r][c] = True

    # 델타 정의 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 목적지 도착 여부 판단 초기값
    ans = 0
    # 현재 위치에서 4방향 이웃을 확인
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]

        # 다음 위치가 격자 범위 안에 있고,
        if 0 <= nr < N and 0 <= nc < N:
            # 그곳이 통로(0)이면서, 아직 방문하지 않았으면
            if maze[nr][nc] != 1 and not visited[nr][nc]:
                # dfs 결과를 더해줌
                ans += dfs(nr, nc)
    return ans


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    # 방문 여부
    visited = [[False] * N for _ in range(N)]

    # 미로 탐색 시작
    for i in range(N):
        for j in range(N):
            # 현재 위치가 출발지일 때
            if maze[i][j] == 2:
                result = dfs(i, j)

    print(f"#{tc} {result}")