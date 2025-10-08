import sys
from collections import deque

line = sys.stdin.readline

# 델타 방향 정의
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

drc = {0: [-1, 0], 1: [0, 1], 2: [1, 0], 3: [0, -1]}

reverse_motion = {0: 2, 1: 3, 2: 0, 3: 1}

rotate_motion = {0: 3, 1: 0, 2: 1, 3: 2}


def bfs():
    global answer
    visited = [[False] * M for _ in range(N)]
    q = deque([(row, col, d)])

    while q:
        cr, cc, cd = q.popleft()

        if room[cr][cc] == 0 and not visited[cr][cc]:
            answer += 1
            visited[cr][cc] = True

        check = False
        for i in range(4):
            nr, nc = cr + dr[i], cc + dc[i]

            if room[nr][nc] == 0 and not visited[nr][nc]:
                check = True
                break

        if not check:
            nr, nc = cr + drc[reverse_motion[cd]][0], cc + drc[reverse_motion[cd]][1]

            if room[nr][nc] == 1:
                break
            else:
                q.append((nr, nc, cd))
        else:
            rd = cd
            for _ in range(4):
                rd = rotate_motion[rd]
                nr, nc = cr + drc[rd][0], cc + drc[rd][1]

                if room[nr][nc] == 0 and not visited[nr][nc]:
                    q.append((nr, nc, rd))
                    break


N, M = map(int, line().split())
row, col, d = map(int, line().split())
room = [list(map(int, line().split())) for _ in range(N)]

answer = 0
bfs()
print(answer)