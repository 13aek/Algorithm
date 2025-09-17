import heapq

# 델타 정의 (상하좌우)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def dijkstra():
    N = len(grid)

    INF = 10**12
    dist = [[INF] * N for _ in range(N)]

    # 시작 칸 비용 기록
    dist[0][0] = grid[0][0]

    pq = []
    heapq.heappush(pq, (grid[0][0], 0, 0))

    while pq:
        cur_cost, r, c = heapq.heappop(pq)

        # 꺼낸 정보가 dist 와 다르면(이미 더 싼 경로가 있었다면) 스킵
        if cur_cost != dist[r][c]:
            continue

        # 목적지에 처음 도달한 순간이 정답
        if r == N - 1 and c == N - 1:
            return cur_cost

        # 이웃 탐색 (상하좌우)
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            # 격자 범위 체크
            if 0 <= nr < N and 0 <= nc < N:
                # 새 누적비용 계산
                new_cost = cur_cost + grid[nr][nc]

                # 더 싸게 갈 수 있으면 갱신
                if new_cost < dist[nr][nc]:
                    dist[nr][nc] = new_cost
                    # 힙에 갱신된 상태 push
                    heapq.heappush(pq, (new_cost, nr, nc))


for tc in range(1, int(input()) + 1):
    N = int(input())
    grid = [list(map(int, input().strip())) for _ in range(N)]
    ans = dijkstra()
    print(f"#{tc} {ans}")
