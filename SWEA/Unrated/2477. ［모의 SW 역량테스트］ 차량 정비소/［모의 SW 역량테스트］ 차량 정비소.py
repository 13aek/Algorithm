for tc in range(1, int(input()) + 1):
    N, M, K, A, B = map(int, input().split())
    reception_desk = list(map(int, input().split()))
    repair_desk = list(map(int, input().split()))
    tk = list(map(int, input().split()))

    ans = 0
    waiting_repair = []
    reception = [-1] * N
    repair = [-1] * M
    reception_num = []
    repair_num = [0] * K

    for customer in range(K):
        check = 0

        for n in range(N):
            if reception[n] < tk[customer]:
                reception[n] = tk[customer] + reception_desk[n] - 1
                reception_num.append(n)
                check = 1
                waiting_repair.append((reception[n] + 1, n, customer))
                break

        if check == 0:
            idx = reception.index(min(reception))
            reception_num.append(idx)
            reception[idx] += reception_desk[idx]
            waiting_repair.append((reception[idx] + 1, idx, customer))

    waiting_repair.sort()

    for w in waiting_repair:
        check = 0

        for m in range(M):
            if repair[m] < w[0]:
                repair[m] = w[0] + repair_desk[m] - 1
                repair_num[w[2]] = m
                check = 1
                break

        if check == 0:
            idx = repair.index(min(repair))
            repair_num[w[2]] = idx
            repair[idx] += repair_desk[idx]

    for k in range(K):
        if (reception_num[k] + 1, repair_num[k] + 1) == (A, B):
            ans += (k + 1)

    print(f"#{tc} {-1 if ans == 0 else ans}")