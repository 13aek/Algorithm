T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))

    max_num = -1

    for i in range(N):
        for j in range(N):
            if i != j:
                is_pass = True
                check_num = str(A[i] * A[j])
                for k in range(len(check_num) - 1):
                    if int(check_num[k]) > int(check_num[k + 1]):
                        is_pass = False
                        break

                if is_pass:
                    max_num = max(max_num, A[i] * A[j])

    print(f"#{tc} {max_num}")