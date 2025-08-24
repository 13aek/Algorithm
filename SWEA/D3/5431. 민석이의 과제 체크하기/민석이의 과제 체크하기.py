T = int(input())

for tc in range(1, T+ 1):
    N, K = map(int, input().split())
    numbers = list(map(int, input().split()))

    idx = [0] * (N + 1)

    for i in numbers:
        idx[i] = 1

    result = []
    for j in range(1, N + 1):
        if idx[j] == 0:
            result += [j]

    print(f"#{tc}", *result)