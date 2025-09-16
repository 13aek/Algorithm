from heapq import heappop, heappush

# 델타 (상하좌우)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dijkstra():
    global min_cost
    pq = []
    # 출발지 연료 코스트, 출발지 높이, 출발지 좌표 (r, c)
    heappush(pq, (0, map_info[0][0], 0, 0))
    # 출발지 비용 기입
    dist[0][0] = 0

    while pq:
        cost, h, r, c = heappop(pq)

        # 기록된 비용이랑 현재 비용이 다르면 무시
        if cost > dist[r][c]:
            continue

        # 갈 수 있는 방향 탐색
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            # 범위 안이고 방문하지 않은 곳일 때
            if 0 <= nr < N and 0 <= nc < N:
                new_cost = cost + 1 + max(0, map_info[nr][nc] - h)     # 다음 비용 계산
                if dist[nr][nc] > new_cost:
                    dist[nr][nc] = new_cost     # 다음 위치 비용 기입
                    heappush(pq, (new_cost, map_info[nr][nc], nr, nc))  # pq에 푸시


for tc in range(1, int(input()) + 1):
    N = int(input())
    map_info = [list(map(int, input().split())) for _ in range(N)]

    # 각 위치당 최저 소비량을 기록할 배열
    dist = [[float('inf')] * N for _ in range(N)]
    dijkstra()
    min_cost = dist[N-1][N-1]
    print(f"#{tc} {min_cost}")