from collections import deque

# 델타 (상하좌우)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs():
    q = deque([(1, 1)])
    visited = set()
    visited.add((1, 1))

    while q:
        cr, cc = q.popleft()

        if miro[cr][cc] == 3:
            return 1

        visited.add((cr, cc))

        for i in range(4):
            nr, nc = cr + dr[i], cc + dc[i]

            if (0 <= nr < 16 and 0 <= nc < 16) and miro[nr][nc] != 1:
                if (nr, nc) not in visited:
                    q.append((nr, nc))

    return 0


for tc in range(1, 11):
    test_cast = int(input())
    miro = [list(map(int, input())) for _ in range(16)]
    print(f"#{tc} {bfs()}")