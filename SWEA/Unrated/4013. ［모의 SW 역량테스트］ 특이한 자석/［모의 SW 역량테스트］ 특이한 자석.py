from collections import deque


def is_rotated(rotate_magnetic, rotate_direction):
    check = [False] * 4
    q = deque()
    q.append((rotate_magnetic, rotate_direction))
    while q:
        m, d = q.popleft()

        if check[m]:
            continue

        check[m] = True

        for nm in adj_list[m]:
            if not check[nm]:
                if nm < m and magnetic_field[nm][2] != magnetic_field[m][6]:
                    q.append((nm, -d))
                elif nm > m and magnetic_field[nm][6] != magnetic_field[m][2]:
                    q.append((nm, -d))

        magnetic_field[m].rotate(d)


for tc in range(1, int(input()) + 1):
    K = int(input())
    magnetic_field = [deque(list(map(int, input().split()))) for _ in range(4)]
    rotate_info = [list(map(int, input().split())) for _ in range(K)]
    adj_list = [[0, 1], [0, 2], [1, 3], [2, 3]]
    for i in range(K):
        rm, rd = rotate_info[i]
        is_rotated(rm - 1, rd)

    score = [1, 2, 4, 8]
    total_score = 0
    for i in range(4):
        total_score += (score[i] * magnetic_field[i][0])

    print(f"#{tc} {total_score}")