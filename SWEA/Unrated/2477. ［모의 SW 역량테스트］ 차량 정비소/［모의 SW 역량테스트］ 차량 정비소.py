from heapq import heapify, heappop, heappush


def bfs():
    ans = 0
    reception = [-1] * (N + 1)
    repair = [-1] * (M + 1)
    waiting_reception = []
    for idx, value in enumerate(tk):
        # (tk, 고객번호, 접수창구방문여부, 수리창구방문여부, 방문한 접수창구, 방문한 수리 창구)
        heappush(waiting_reception, (value, idx + 1, 0, 0))
    waiting_repair = []

    while waiting_reception:
        cur_time, customer, is_reception, is_repair = heappop(waiting_reception)

        # 1. 아직 접수창구에 방문하지 않았으면
        # 1.1 접수 창구에 자리가 있으면
        if any(reception[i] < cur_time for i in range(1, N+1)):
            for i in range(1, N + 1):
                if reception[i] < cur_time:
                    reception[i] = cur_time + reception_desk[i] - 1
                    heappush(waiting_repair, (reception[i] + 1, i, customer))
                    break
        # 1.2 접수 창구에 자리가 없으면
        else:
            idx = min(range(1, N+1), key=lambda x: reception[x])
            reception[idx] += reception_desk[idx]
            heappush(waiting_repair, (reception[idx] + 1, idx, customer))

    while waiting_repair:
        cur_time, rcp_num, customer = heappop(waiting_repair)

        # 2. 아직 수리 창구에 방문하지 않았으면
        # 2.1 수리 창구에 자리가 있으면
        if any(repair[i] < cur_time for i in range(1, M+1)):
            for i in range(1, M + 1):
                if repair[i] < cur_time:
                    repair[i] = cur_time + repair_desk[i] - 1
                    if (rcp_num, i) == (A, B):
                        ans += customer
                    break
        # 2.2 수리 창구에 자리가 없으면
        else:
            idx = min(range(1, M+1), key=lambda x: repair[x])
            repair[idx] += repair_desk[idx]
            if (rcp_num, idx) == (A, B):
                ans += customer

    return -1 if ans == 0 else ans


for tc in range(1, int(input()) + 1):
    N, M, K, A, B = map(int, input().split())
    reception_desk = [-1] + list(map(int, input().split()))
    repair_desk = [-1] + list(map(int, input().split()))
    tk = list(map(int, input().split()))

    result = bfs()
    print(f"#{tc} {result}")