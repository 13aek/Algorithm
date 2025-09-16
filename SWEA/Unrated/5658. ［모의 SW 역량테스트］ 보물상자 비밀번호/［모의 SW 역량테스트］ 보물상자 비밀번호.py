from collections import deque

for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    numbers = list(input())
    n = N // 4      # 한 변에 들어가는 개수

    password_comb = set()

    i = 0
    while i < n:
        num = deque(numbers)
        num.rotate(-i)
        hexadecimal = ''
        while num:
            hexadecimal += num.popleft()

            if len(hexadecimal) == n:
                password_comb.add((hexadecimal, int(hexadecimal, 16)))
                hexadecimal = ''

        i += 1

    pw = list(password_comb)
    pw.sort(key=lambda x: x[1], reverse=True)

    print(f"#{tc} {pw[K-1][1]}")