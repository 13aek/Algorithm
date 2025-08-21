import itertools

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = [list(map(int, input().split())) for _ in range(N)]

    minimum = float('inf')

    col = list(range(N))

    for c in itertools.permutations(col):
        current_sum = 0
        for r in range(N):
            col_idx = c[r]
            current_sum += numbers[r][col_idx]
            if current_sum > minimum:
                break

        minimum = min(minimum, current_sum)

    print(f"#{tc} {minimum}")