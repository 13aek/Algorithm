for tc in range(1, 11):
    N = int(input())
    # 자성체들이 놓여있는 테이블을 입력 받음
    table = [list(map(int, input().split())) for _ in range(N)]

    # 교착상태 횟수의 초기값
    deadlock_count = 0

    # 테이블을 순회하는 for 문 (열 우선 순회)
    for c in range(N):
        stack = []
        for r in range(N):

            if table[r][c] == 0:
                continue

            elif table[r][c] == 1:

                if stack and stack[-1] == 1:
                    continue

                stack.append(table[r][c])

            elif table[r][c] == 2:

                if stack and stack[-1] == 1:
                    stack.pop()
                    deadlock_count += 1

    print(f"#{tc} {deadlock_count}")