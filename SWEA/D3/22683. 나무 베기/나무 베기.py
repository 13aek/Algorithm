from heapq import heappush, heappop

# 델타 방향 정의 (상하좌우)
drc = {0: (-1, 0), 1: (1, 0), 3: (0, -1), 4: (0, 1)}


def bfs():
    global min_cnt
    best = {}
    result = set()
    pq = []
    for r in range(N):
        for c in range(N):
            if field[r][c] == 'X':
                heappush(pq, (0, K, 0, r, c))
                best[(r, c, 0, K)] = 0
            if field[r][c] == 'Y':
                result.add((r, c))

    while pq:
        cur_cnt, cur_k, cur_d, cr, cc = heappop(pq)

        key = (cr, cc, cur_d, cur_k)
        if best.get(key, float('inf')) < cur_cnt:
            continue

        if (cr, cc) in result:
            min_cnt = cur_cnt
            return

        for i in [0, 1, 3, 4]:
            nr, nc = cr + drc[i][0], cc + drc[i][1]

            if 0 <= nr < N and 0 <= nc < N:
                if field[nr][nc] != 'T':
                    if cur_d == i:
                        ncost, nk, nd = cur_cnt + 1, cur_k, cur_d
                    elif abs(cur_d - i) == 1:
                        ncost, nk, nd = cur_cnt + 3, cur_k, i
                    else:
                        ncost, nk, nd = cur_cnt + 2, cur_k, i
                else:
                    if cur_k:
                        if cur_d == i:
                            ncost, nk, nd = cur_cnt + 1, cur_k - 1, cur_d
                        elif abs(cur_d - i) == 1:
                            ncost, nk, nd = cur_cnt + 3, cur_k - 1, i
                        else:
                            ncost, nk, nd = cur_cnt + 2, cur_k - 1, i
                    else:
                        continue

                nkey = (nr, nc, nd, nk)
                if ncost < best.get(nkey, float('inf')):
                    best[nkey] = ncost
                    heappush(pq, (ncost, nk, nd, nr, nc))


for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    field = [list(input()) for _ in range(N)]
    min_cnt = float('inf')
    bfs()
    print(f"#{tc} {-1 if min_cnt == float('inf') else min_cnt}")