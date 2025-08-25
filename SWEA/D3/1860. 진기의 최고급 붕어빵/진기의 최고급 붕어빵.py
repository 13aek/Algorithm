T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    customer_visit_time = list(map(int, input().split()))
    bread = [0] * (max(customer_visit_time) + 1)

    possible = 'Possible'
    for i in range(1, len(bread)):
        if i % M == 0:
            bread[i] += K

        bread[i] += bread[i - 1]

        if i in customer_visit_time:
            for j in customer_visit_time:
                if j == i:
                    bread[i] -= 1

            if bread[i] < 0:
                possible = 'Impossible'
                break

    if 0 in customer_visit_time:
        possible = 'Impossible'

    print(f"#{tc} {possible}")