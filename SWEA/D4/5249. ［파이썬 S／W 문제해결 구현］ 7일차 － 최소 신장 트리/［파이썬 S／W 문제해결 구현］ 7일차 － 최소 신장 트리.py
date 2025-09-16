from heapq import heappush, heappop


def prim_mst(start=0):
    global mst_cost
    visited = [False] * (V + 1)
    pq = []

    edges_count = 0

    for cost, next_node in adj_list[start]:
        heappush(pq, (cost, start, next_node))

    visited[start] = True

    while pq and edges_count < V:
        cost, _, end = heappop(pq)

        if visited[end]:
            continue

        visited[end] = True
        mst_cost += cost
        edges_count += 1

        for next_cost, next_node in adj_list[end]:
            if not visited[next_node]:
                heappush(pq, (next_cost, end, next_node))


for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    adj_list = [[] for _ in range(V + 1)]
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        adj_list[n1].append([w, n2])
        adj_list[n2].append([w, n1])

    mst_cost = 0
    prim_mst()
    print(f"#{tc} {mst_cost}")