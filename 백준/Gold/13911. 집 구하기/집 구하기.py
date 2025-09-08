import sys
from heapq import heappop, heappush


def dijkstra(start_nodes, lim):
    dist = [float('inf')] * (V + 1)
    pq = []

    for s in start_nodes:
        if dist[s] > 0:
            dist[s] = 0
            heappush(pq, (0, s))

    while pq:
        d, u = heappop(pq)

        if d > dist[u]:
            continue

        for v, w in adj_list[u]:
            nd = d + w
            if nd < dist[v]:
                if nd <= lim:
                    dist[v] = nd
                    heappush(pq, (nd, v))

    return dist


line = sys.stdin.readline

V, E = map(int, line().split())

adj_list = [[] for _ in range(V + 1)]
for i in range(E):
    u, v, w = map(int, map(int, line().split()))
    adj_list[u].append((v, w))
    adj_list[v].append((u, w))

M, x = map(int, line().split())
m_v = list(map(int, line().split()))
S, y = map(int, line().split())
s_v = list(map(int, line().split()))

is_store = [False] * (V + 1)
for a in m_v:
    is_store[a] = True
for b in s_v:
    is_store[b] = True

dm = dijkstra(m_v, x)
ds = dijkstra(s_v, y)

ans = float('inf')
for v in range(1, V+1):
    if is_store[v]:
        continue
    if dm[v] <= x and ds[v] <= y:
        s = dm[v] + ds[v]
        if s < ans:
            ans = s

print(-1 if ans == float('inf') else ans)