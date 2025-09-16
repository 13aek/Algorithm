from heapq import heappush, heappop


def dijkstra():
    pq = []
    for weight, e in adj_list[0]:
        heappush(pq, (weight, e))
    dist[0] = 0

    while pq:
        cur_w, end = heappop(pq)

        if cur_w > dist[end]:
            continue

        if end == N:
            return

        for n_w, next_node in adj_list[end]:
            new_weight = cur_w + n_w
            if new_weight < dist[next_node]:
                dist[next_node] = new_weight
                heappush(pq, (new_weight, next_node))


for tc in range(1, int(input()) + 1):
    N, E = map(int, input().split())
    adj_list = [[] for _ in range(N + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj_list[s].append([w, e])

    dist = [float('inf')] * (N + 1)
    dijkstra()
    min_cost = dist[N]
    print(f"#{tc} {min_cost}")