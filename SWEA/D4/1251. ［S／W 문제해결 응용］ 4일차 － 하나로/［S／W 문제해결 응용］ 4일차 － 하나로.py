from heapq import heappush, heappop


def dist(x1, y1, x2, y2):
    """
    두 섬간의 유클리드 거리를 반환하는 함수
    """
    return (x1 - x2)**2 + (y1 - y2)**2


def tax(x1, y1, x2, y2):
    """
    두 섬을 연결한 다리의 거리에 따른 세율을 반환하는 함수
    """
    return E * (dist(x1, y1, x2, y2))


def prim():
    visited = [False] * N    # 방문 표시
    distance = [float('inf')] * N   # 각 섬에 도착했을 때 최소 세율
    edges_count = 0     # 간선 수
    min_tax = 0  # 최소 세율

    # 현재코스트, 현재 섬
    pq = [(0, 0)]

    # 첫번째 섬 세율 표시
    distance[0] = 0

    while pq and edges_count < N:
        cost, ci = heappop(pq)

        # 도착섬에 이미 방문했다면 무시
        if visited[ci]:
            continue

        # 방문하지 않은 섬이면 방문 표시
        visited[ci] = True
        min_tax += cost     # 세율에 더해줌
        edges_count += 1    # 간선 수 + 1

        # 현재 도착섬에서 연결할 수 있는 다음 섬이 방문하지 않은 곳이라면 힙에 추가
        for ni in range(N):
            if not visited[ni]:
                nc = tax(island_x[ci], island_y[ci], island_x[ni], island_y[ni])
                if nc < distance[ni]:
                    distance[ni] = nc
                    heappush(pq, (nc, ni))

    return min_tax


for tc in range(1, int(input()) + 1):
    N = int(input())
    island_x = list(map(int, input().split()))
    island_y = list(map(int, input().split()))
    E = float(input())

    ans = prim()
    print(f"#{tc} {round(ans)}")
