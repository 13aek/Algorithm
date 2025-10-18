# 델타 방향 정의 (x 상 우 하 좌)
drc = {0: (0, 0), 1: (0, -1), 2: (1, 0), 3: (0, 1), 4: (-1, 0)}


# 접속 여부 확인 함수
def is_connected(x1, y1, x2, y2, c):
    D = abs(x1 - x2) + abs(y1 - y2)
    if D <= c:
        return True
    else:
        return False


def simulate():
    a = (1, 1)
    b = (10, 10)
    t = 0
    charge_sum = 0

    while t < M + 1:
        xa, ya = a
        xb, yb = b

        # 1. 현재 위치에서 충전 여부 확인
        check_a = set()
        check_b = set()
        for k, v in BC.items():
            cx, cy, c, p = v

            if is_connected(xa, ya, cx, cy, c):
                check_a.add(k)

            if is_connected(xb, yb, cx, cy, c):
                check_b.add(k)

        # 2. 충전량 추가
        if check_a or check_b:

            # 2.1 충전 위치가 겹치지 않으면
            if not check_a & check_b:
                charge_a = max(list(BC[idx][3] for idx in check_a)) if check_a else 0
                charge_b = max(list(BC[idx][3] for idx in check_b)) if check_b else 0
                charge_sum = charge_sum + charge_a + charge_b

            # 2.2 충전 위치가 겹친다면
            elif len(check_a | check_b) == 1:
                idx = list(check_a)
                charge_sum += BC[idx[0]][3]

            elif len(check_a | check_b) > 1:
                charge_max = 0
                for i in check_a:
                    pa = BC[i][3]
                    for j in check_b:
                        pb = BC[j][3]
                        if i == j:
                            if pa > charge_max:
                                charge_max = pa
                        else:
                            if pa + pb > charge_max:
                                charge_max = pa + pb
                charge_sum += charge_max

        # 3. 다음 위치로 이동
        if t == M:
            break

        nxa, nya = xa + drc[user_a[t]][0], ya + drc[user_a[t]][1]
        nxb, nyb = xb + drc[user_b[t]][0], yb + drc[user_b[t]][1]
        a = (nxa, nya)
        b = (nxb, nyb)

        t += 1

    return charge_sum


for tc in range(1, int(input()) + 1):
    M, A = map(int, input().split())
    user_a = list(map(int, input().split()))
    user_b = list(map(int, input().split()))
    BC = {}
    for i in range(1, A + 1):
        x, y, C, P = list(map(int, input().split()))
        BC[i] = [x, y, C, P]

    result = simulate()
    print(f"#{tc} {result}")