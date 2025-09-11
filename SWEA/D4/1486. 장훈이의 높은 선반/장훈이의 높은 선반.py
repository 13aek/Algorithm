from itertools import combinations


def permute():
    global min_h
    for i in range(1, N + 1):
        for perm in combinations(Hi, i):
            if sum(perm) == B:
                min_h = 0
                return

            if sum(perm) > B:
                min_h = min(min_h, sum(perm) - B)


T = int(input())

for tc in range(1, T + 1):
    N, B = map(int, input().split())
    Hi = list(map(int, input().split()))

    min_h = float('inf')
    permute()
    print(f"#{tc} {min_h}")