import sys
from collections import deque, defaultdict
from heapq import heappop, heappush

line = sys.stdin.readline

# 델타 방향 정의 (상하좌우)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def build_bridge(arr, n, m, transpose):
    if not transpose:
        for r in range(n):
            cn = 0
            zero_cnt = 0
            for c in range(m):
                if arr[r][c] == 1:
                    if cn == 0:
                        cn = island[r][c]
                    else:
                        nn = island[r][c]
                        if zero_cnt >= 2 and cn != nn:
                            if connected[cn][nn] > zero_cnt:
                                connected[cn][nn] = zero_cnt
                                connected[nn][cn] = zero_cnt
                        zero_cnt = 0
                        cn = nn
                else:
                    if cn != 0:
                        zero_cnt += 1
    else:
        for c in range(m):
            cn = 0
            zero_cnt = 0
            for r in range(n):
                if arr[r][c] == 1:
                    if cn == 0:
                        cn = island[r][c]
                    else:
                        nn = island[r][c]
                        if zero_cnt >= 2 and cn != nn:
                            if connected[cn][nn] > zero_cnt:
                                connected[cn][nn] = zero_cnt
                                connected[nn][cn] = zero_cnt
                        zero_cnt = 0
                        cn = nn
                else:
                    if cn != 0:
                        zero_cnt += 1


def prim():
    cost = 0
    visited = [False] * num
    edge = 0
    pq = []
    for i in range(1, num):
        if adj_list[i]:
            start = i
            for distance, node in adj_list[i]:
                heappush(pq, (distance, node))
            break
    visited[start] = True

    while pq and edge < num - 2:
        d, end = heappop(pq)

        if visited[end]:
            continue

        visited[end] = True
        cost += d
        edge += 1

        for next_cost, next_node in adj_list[end]:
            if not visited[next_node]:
                heappush(pq, (next_cost, next_node))

    return cost if False not in visited[1:] else -1


N, M = map(int, line().split())
map_info = [list(map(int, line().split())) for _ in range(N)]

island = [[0] * M for _ in range(N)]
check = set()
num = 1
for r in range(N):
    for c in range(M):
        if map_info[r][c] != 0 and (r, c) not in check:
            island[r][c] = num
            check.add((r, c))
            q = deque([(r, c)])

            while q:
                cr, cc = q.popleft()

                for i in range(4):
                    nr, nc = cr + dr[i], cc + dc[i]

                    if (0 <= nr < N and 0 <= nc < M) and map_info[nr][nc] != 0 and (nr, nc) not in check:
                        q.append((nr, nc))
                        island[nr][nc] = num
                        check.add((nr, nc))
            num += 1

connected = [[float('inf')] * num for _ in range(num)]

adj_list = [[] for _ in range(num)]
build_bridge(map_info, N, M, False)
build_bridge(map_info, N, M, True)
for i in range(1, num):
    for j in range(1, num):
        if connected[i][j] != float('inf'):
            adj_list[i].append([connected[i][j], j])

if any(adj_list):
    result = prim()
    print(result)
else:
    print(-1)