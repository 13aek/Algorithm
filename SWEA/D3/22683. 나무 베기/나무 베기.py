from heapq import heappush, heappop

# 델타 방향 정의 (상우하좌)
drc = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}


def rot_cost(d, nd):
    delta = (nd - d) % 4
    rot = min(delta, 4 - delta)
    return rot + 1


def bfs():
    global min_cnt
    best = {}
    destination = ()
    pq = []
    for r in range(N):
        for c in range(N):
            if field[r][c] == 'X':
                best[(r, c, 0, K)] = 0
                heappush(pq, (0, K, 0, r, c))
            if field[r][c] == 'Y':
                destination = (r, c)
    INF = float('inf')

    while pq:
        cur_cnt, cur_k, cur_d, cr, cc = heappop(pq)

        key = (cr, cc, cur_d, cur_k)
        if best.get(key, INF) < cur_cnt:
            continue

        if (cr, cc) == destination:
            min_cnt = cur_cnt
            return

        for i in range(4):
            nr, nc = cr + drc[i][0], cc + drc[i][1]

            if 0 <= nr < N and 0 <= nc < N:
                cost = rot_cost(cur_d, i)
                if field[nr][nc] != 'T':
                    ncost, nk = cur_cnt + cost, cur_k
                else:
                    if not cur_k:
                        continue
                    ncost, nk = cur_cnt + cost, cur_k - 1

                nkey = (nr, nc, i, nk)
                if ncost < best.get(nkey, INF):
                    best[nkey] = ncost
                    heappush(pq, (ncost, nk, i, nr, nc))


for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    field = [list(input()) for _ in range(N)]
    min_cnt = float('inf')
    bfs()
    print(f"#{tc} {-1 if min_cnt == float('inf') else min_cnt}")