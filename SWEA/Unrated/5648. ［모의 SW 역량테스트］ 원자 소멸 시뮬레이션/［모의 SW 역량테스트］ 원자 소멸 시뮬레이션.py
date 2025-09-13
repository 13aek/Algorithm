# 델타 방향 정의 (상 하 좌 우)
drc = [(0, 1), (0, -1), (-1, 0), (1, 0)]


def simulate(dic):
    global energy_burst

    cur_pp = power_plant

    while cur_pp:

        next_pp = {}

        # 1초 후 원자 일괄 이동
        for (x, y), (d, e) in cur_pp.items():
            nx, ny = x + drc[d][0], y + drc[d][1]

            # 경계 밖 원자는 소멸
            if -2000 > nx or nx > 2000 or -2000 > ny or ny > 2000:
                continue

            key = (nx, ny)
            # 1. next_pp 에 이미 있는 경우 (충돌) 합쳐줌
            if key in next_pp:
                next_pp[key][0] += e    # energy
                next_pp[key][1] += 1    # count

            # 2. next_pp 에 들어가 있지 않은 경우
            else:
                # energy 합, count (해당 위치 원자 개수), 진행방향
                next_pp[key] = [e, 1, d]

        # 원자 일괄 이동이 끝나고 다음 원자 구성
        cur_pp = {}
        for position, (e_sum, cnt, direction) in next_pp.items():
            # 해당 위치의 원자 개수가 1개 초과일 때 (충돌했을 경우)
            if cnt > 1:
                energy_burst += e_sum
            # 충돌이 없을 때
            else:
                cur_pp[position] = (direction, e_sum)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    atomic_info = [list(map(int, input().split())) for _ in range(N)]

    # 0.5초 충돌 계산을 위해 좌표값을 2배로 딕셔너리에 저장장
    power_plant = {}
    for a, b, d, c in atomic_info:
        power_plant[(a * 2, b * 2)] = [d, c]

    energy_burst = 0

    simulate(power_plant)

    print(f"#{tc} {energy_burst}")