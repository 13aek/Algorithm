def backtracking(lst, idx, charge_cnt, distance):
    global result
    # 조기 종료 조건
    # 1. 결과값보다 현재 충전 횟수가 더 많으면
    if charge_cnt >= result:
        return

    for d in range(distance, 0, -1):
        if idx + d >= info[0]:
            if charge_cnt < result:
                result = charge_cnt
                return
        backtracking(lst, idx + d, charge_cnt + 1, lst[idx+d])


T = int(input())

for tc in range(1, T+1):
    info = list(map(int, input().split()))

    bus_stop = [0] * (info[0] + 1)
    for i in range(1, info[0]):
        bus_stop[i] = info[i]

    result = float('inf')

    backtracking(bus_stop, 1, 0, bus_stop[1])
    print(f"#{tc} {result}")