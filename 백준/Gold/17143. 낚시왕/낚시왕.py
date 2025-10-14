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

        # 1. 낚시왕 한 칸 이동
        king += 1

        # 2. 낚시 시도
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

        # 2.1 낚시킹이 가장 오른쪽열에서 낚시를 마쳤으면 중지
        if king == C:
            break

        # 3. 상어 이동
        for k, v in shark.items():
            cr, cc = k
            s, d, z = v
            if d == 1 or d == 2:
                ns = s % ((R - 1) * 2)
            else:
                ns = s % ((C - 1) * 2)
            nd = d
            nr, nc = cr, cc
            for distance in range(1, ns + 1):
                nr, nc = nr + drc[nd][0], nc + drc[nd][1]

                if nr < 1 or nr > R or nc < 1 or nc > C:
                    nd = opposite[nd]
                    nr, nc = nr + drc[nd][0] * 2, nc + drc[nd][1] * 2

            # bucket 에 다음 상어 위치 저장
            # 3.1 상어가 같은 위치에 있는 경우
            if (nr, nc) in bucket:
                es, ed, ez = bucket[(nr, nc)]
                if z > ez:
                    bucket[(nr, nc)] = [s, nd, z]
            # 3.2 해당 위치에 아무 상어도 없을 경우
            else:
                bucket[(nr, nc)] = [s, nd, z]

        shark = bucket

    return fishing


R, C, M = map(int, line().split())
sharks = {}
for _ in range(M):
    r, c, s, d, z = map(int, line().split())
    sharks[(r, c)] = [s, d, z]   # 속력, 이동 방향, 크기

print(simulate(sharks))