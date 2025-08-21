# [Unrated] [모의 SW 역량테스트] 등산로 조성 - 1949 

[문제 링크](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PoOKKAPIDFAUq) 

### 성능 요약

메모리: 63,360 KB, 시간: 144 ms, 코드길이: 1,962 Bytes

### 제출 일자

2025-08-21 15:07

### 처음 푼 코드 (지금 py파일은 어느 정도 코드 정리 한 버전)
메모리: 63,360 kb, 시간: 152 ms, 코드길이: 2,628 Bytes
```python
# 델타 탐색해서 길이를 산봉우리 하나에서 가장 긴 등산로를 반환하는 함수
def long_road(arr, row, col, k, delta=4):
    """
    이중배열과 가장 높은 산봉우리의 위치 (row, col)을 인자로 받아서
    그 산봉우리에서 가장 긴 등산로의 길이를 반환해주는 함수
    """
    max_dis = 1
    x = row
    y = col
    k_value = k
    for d in range(4):
        distance = 1
        nr = x + dr[d]
        nc = y + dc[d]

        if (0 <= nr < N and 0 <= nc < N) and visited[nr][nc] is False:
            if arr[nr][nc] < arr[x][y]:
                visited[nr][nc] = True
                distance += long_road(arr, nr, nc, k_value, d)
                visited[nr][nc] = False
            elif arr[nr][nc] >= arr[x][y]:
                if k_value:
                    for j in range(1, k_value + 1):
                        if arr[nr][nc] - j < arr[x][y]:
                            arr[nr][nc] -= j
                            visited[nr][nc] = True
                            distance += long_road(arr, nr, nc, 0, d)
                            visited[nr][nc] = False
                            arr[nr][nc] += j
                            break
            if distance > max_dis:
                max_dis = distance

    return max_dis


# 델타 방향 정의 (상, 하, 좌, 우)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    mountain_map = [list(map(int, input().split())) for _ in range(N)]

    # 가장 높은 산봉우리가 붙어 있을 경우 그 산봉우리를 k개 만큼 깎음
    # 일단 k개 만큼 공사를 하기 전 최장 등산로 길이를 탐색하는 거부터
    # 높은 산봉우리에서 상하좌우 탐색
    # 탐색 후 현재 위치보다 낮으면 한칸 이동
    # 만약 이동할 곳이 없을 때 k 가 0이 아니면 이동할 칸에 - k 하고 이동
    # k가 0 이거나 이동할 곳이 없으면 이동한 거리를 저장하고 종료
    # 이동한 루트는 스택에 쌓아서 넣는 방식으로
    # 이전 최장 거리 값이랑 비교해서 더 길면 갱신
    # 모든 산봉우리의 루트를 탐색했으면 종료

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
            # 만약 현재 위치가 가장 높은 위치의 산봉우리면
            if mountain_map[r][c] == maximum:
                visited[r][c] = True
                length = long_road(mountain_map, r, c, K)
                if length > max_length:
                    max_length = length
                visited[r][c] = False

    print(f"#{tc} {max_length}")
```


> 출처: SW Expert Academy, https://swexpertacademy.com/main/code/problem/problemList.do
