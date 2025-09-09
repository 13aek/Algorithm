T = int(input())

for tc in range(1, T+1):
    A, B, C = map(int, input().split())

    eat_candy = 0
    while B > C - 1:
        if B - 1 == 1:
            break
        B -= 1
        eat_candy += 1

    while A > B - 1:
        if A - 1 < 1:
            break
        A -= 1
        eat_candy += 1

    print(f"#{tc} ", end='')
    print(-1 if not A < B < C else eat_candy)