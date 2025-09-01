T = int(input())

for tc in range(1, T+1):
    N = int(input())
    alpha = list(input().split())

    result = []
    if N % 2 == 0:
        for i in range(N//2):
            result.append(alpha[:N//2][i])
            result.append(alpha[N//2:][i])
    else:
        for i in range(N//2):
            result.append(alpha[:N//2][i])
            result.append(alpha[N//2 + 1:][i])
        result.append(alpha[N//2])

    print(f"#{tc}", *result)