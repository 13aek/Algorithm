for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    a = 2*m - n
    b = n - m
    print(f"#{tc} {a} {b}")