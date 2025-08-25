# 델타 탐색해서 길이를 산봉우리 하나에서 가장 긴 등산로를 반환하는 함수
def long_road(arr, x, y, k, delta=4):
    """ 
    이중배열과 가장 높은 산봉우리의 위치 row, col을 인자로 받아서
    그 산봉우리에서 가장 긴 등산로의 길이를 반환 
    """
    max_dis = 1
    for d in range(4):
        distance = 1
        nr = x + dr[d]
        nc = y + dc[d]

        if (0 <= nr < N and 0 <= nc < N) and visited[nr][nc] is False:
            if arr[nr][nc] < arr[x][y]:
                visited[nr][nc] = True
                max_dis = max(max_dis, 1 + long_road(arr, nr, nc, k, d))
                visited[nr][nc] = False
            elif arr[nr][nc] >= arr[x][y]:
                if k:
                    for j in range(1, k + 1):
                        if arr[nr][nc] - j < arr[x][y]:
                            arr[nr][nc] -= j
                            visited[nr][nc] = True
                            max_dis = max(max_dis, 1 + long_road(arr, nr, nc, 0, d))
                            visited[nr][nc] = False
                            arr[nr][nc] += j
                            break
    return max_dis


# 델타 방향 정의 (상, 하, 좌, 우)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    mountain_map = [list(map(int, input().split())) for _ in range(N)]

    # 가장 높은 산봉우리의 높이를 찾음
    maximum = 0
    for i in mountain_map:
        maximum = max(maximum, max(i))

    # 최장 거리를 저장할 초기값
    max_length = 0

    # 방문한 곳인지 표시
    visited = [[False] * N for _ in range(N)]

    # 등산로 배열을 탐색
    for r in range(N):
        for c in range(N):
            # 현재 위치가 가장 높은 위치의 산봉우리면
            if mountain_map[r][c] == maximum:
                visited[r][c] = True
                max_length = max(max_length, long_road(mountain_map, r, c, K))
                visited[r][c] = False

    print(f"#{tc} {max_length}")