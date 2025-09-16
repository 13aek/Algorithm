from collections import deque

# 델타 방향 정의 (상하좌우)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs():
    global alive
    start_t = 1
    q = []
    for r in range(N):
        for c in range(M):
            if grid[r][c] != 0:
                # 생명력 수치, 현재 시간, 활성화 시간, 위치, 활성화 상태
                q.append((grid[r][c], start_t, grid[r][c], r, c, False))
                visited.add((r, c))
    lst = sorted(q, key=lambda x: x[0], reverse=True)
    dq = deque(lst)

    while dq:
        hp, t, active_t, x, y, is_active = dq.popleft()

        # 1. 생명력이 다했으면 빼줌
        if is_active:
            if t - active_t == hp:
                continue
            elif t - active_t < hp:
                dq.append((hp, t + 1, active_t, x, y, True))
                continue

        # 2. 현재시간이 주어진 K와 같아졌을 때
        if t == K:
            cnt = 1
            for i in range(len(dq)):
                if dq[i][1] > K:
                    cnt += 1
                    continue
                if dq[i][1] - dq[i][2] < dq[i][0]:
                    cnt += 1
            alive = cnt
            return

        # 3. 활성화 시간이 안왔으면 시간만 늘려주고 푸시
        if t < active_t:
            dq.append((hp, t + 1, active_t, x, y, False))
            continue

        # 4. 현재 시간이 활성화 시간이랑 같으면 활성화 상태로 변경 후 자기자신 및 번식 칸 q에 추가
        if t == active_t and not is_active:
            dq.append((hp, t + 1, active_t, x, y, True))

            for i in range(4):
                nr, nc = x + dr[i], y + dc[i]

                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    dq.append((hp, t + 1, t + 1 + hp, nr, nc, False))


for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    visited = set()
    alive = 0
    bfs()
    print(f"#{tc} {alive}")
