from collections import deque

# 델타 방향 정의 (상하좌우)
drc = {0: (-1, 0), 1: (1, 0), 2: (0, -1), 3: (0, 1)}


def bfs(lst):
    delta = deque([0, 3, 1, 2])
    q = deque()
    result = set()
    for r in range(N):
        for c in range(N):
            if field[r][c] == 'X':
                q.append((delta[0], r, c))
            elif field[r][c] == 'Y':
                result.add((r, c))

    current_command = deque(lst)

    while q:
        d, cr, cc = q.popleft()

        if current_command:
            cur_com = current_command.popleft()
            if cur_com == 'L':
                delta.rotate(1)
                q.append((delta[0], cr, cc))
            elif cur_com == 'R':
                delta.rotate(-1)
                q.append((delta[0], cr, cc))
            elif cur_com == 'A':
                nr, nc = cr + drc[d][0], cc + drc[d][1]

                if 0 <= nr < N and 0 <= nc < N:
                    if field_copy[nr][nc] == 'G' or field_copy[nr][nc] == 'Y':
                        field_copy[cr][cc] = 'G'
                        field_copy[nr][nc] = 'X'
                        q.append((d, nr, nc))
                    elif field_copy[nr][nc] == 'T':
                        q.append((d, cr, cc))
                else:
                    q.append((d, cr, cc))
        else:
            result.add((cr, cc))

    return len(result) == 1


for tc in range(1, int(input()) + 1):
    N = int(input())
    field = [list(input()) for _ in range(N)]
    Q = int(input())
    C = [list(input().split()) for _ in range(Q)]

    is_arrived = []
    for n, command in C:
        field_copy = [row[:] for row in field]
        cur_c = list(command)
        if bfs(cur_c):
            is_arrived.append(1)
        else:
            is_arrived.append(0)

    print(f"#{tc}", *is_arrived)