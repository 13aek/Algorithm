import sys

line = sys.stdin.readline

# 델타 방향 정의 (상하우좌)
drc = {1: (-1, 0), 2: (1, 0), 3: (0, 1), 4: (0, -1)}

# 반대 방향 정의
opposite = {1: 2, 2: 1, 3: 4, 4: 3}


def simulate(shark):
    king = 0
    fishing = 0
    while shark:
        bucket = {}
        king += 1

        candidate = False
        candi_row = float('inf')
        for key in shark.keys():
            if key[1] == king:
                if candi_row > key[0]:
                    candidate = key
                    candi_row = key[0]
        if candidate:
            fishing += shark[candidate][2]
            del shark[candidate]

        if king == C:
            break

        # 2. 상어 이동 (수식 기반 O(1))
        for (r, c), (s, d, z) in shark.items():
            if d == 1 or d == 2:  # 상하 이동
                cycle = (R - 1) * 2
                move = s % cycle
                if d == 1:
                    nr = r - move
                    if nr < 1:
                        nr = 2 - nr
                        d = 2
                    if nr > R:
                        nr = 2 * R - nr
                        d = 1
                else:
                    nr = r + move
                    if nr > R:
                        nr = 2 * R - nr
                        d = 1
                    if nr < 1:
                        nr = 2 - nr
                        d = 2
                nc = c

            else:  # 좌우 이동
                cycle = (C - 1) * 2
                move = s % cycle
                if d == 4:
                    nc = c - move
                    if nc < 1:
                        nc = 2 - nc
                        d = 3
                    if nc > C:
                        nc = 2 * C - nc
                        d = 4
                else:
                    nc = c + move
                    if nc > C:
                        nc = 2 * C - nc
                        d = 4
                    if nc < 1:
                        nc = 2 - nc
                        d = 3
                nr = r

            if (nr, nc) in bucket:
                if z > bucket[(nr, nc)][2]:
                    bucket[(nr, nc)] = [s, d, z]
            else:
                bucket[(nr, nc)] = [s, d, z]

        shark = bucket

    return fishing


R, C, M = map(int, line().split())
sharks = {}
for _ in range(M):
    r, c, s, d, z = map(int, line().split())
    sharks[(r, c)] = [s, d, z]  # 속력, 이동 방향, 크기

print(simulate(sharks))