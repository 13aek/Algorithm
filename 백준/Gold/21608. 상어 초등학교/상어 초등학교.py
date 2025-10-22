import sys
from collections import defaultdict

line = sys.stdin.readline

# 델타 방향 정의 (상하좌우)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def search_blank():
    max_blank = -1
    best_pos = (-1, -1)

    for r in range(N):
        for c in range(N):
            if classroom[r][c] != 0:
                continue  # 이미 자리가 찼으면 패스

            blank_cnt = 0
            for k in range(4):
                nr, nc = r + dr[k], c + dc[k]
                if (0 <= nr < N and 0 <= nc < N) and classroom[nr][nc] == 0:
                    blank_cnt += 1

            # 1. 인접 빈칸 수가 더 많거나
            # 2. 같을 때는 행 번호가 작고
            # 3. 또 같으면 열 번호가 작은 칸을 우선
            if blank_cnt > max_blank or \
               (blank_cnt == max_blank and (r, c) < best_pos):
                max_blank = blank_cnt
                best_pos = (r, c)

    return best_pos


N = int(line())
classroom = [[0] * N for _ in range(N)]
info = []
student_info = {}
for _ in range(N * N):
    num, a, b, c, d = map(int, line().split())
    info.append(num)
    student_info[num] = [a, b, c, d]

possible_position = defaultdict(set)
classroom[1][1] = info[0]

for i in range(4):
    r, c = 1 + dr[i], 1 + dc[i]
    if 0 <= r < N and 0 <= c < N:
        possible_position[info[0]].add((r, c))

for i in range(1, N * N):
    cur_student = info[i]
    prefer = student_info[cur_student]
    candidate = {}

    for p in prefer:
        if p in possible_position:
            for (r, c) in possible_position[p]:
                if (r, c) not in candidate:
                    if classroom[r][c] == 0:
                        cnt = 1
                        blank = 0
                        for i in range(4):
                            nr, nc = r + dr[i], c + dc[i]

                            if (0 <= nr < N and 0 <= nc < N) and classroom[nr][nc] == 0:
                                blank += 1

                        candidate[(r, c)] = [cnt, blank]
                else:
                    cnt, blank = candidate[(r, c)]
                    candidate[(r, c)] = [cnt + 1, blank]

    if candidate:
        key, value = next(iter(sorted(candidate.items(), key=lambda x: (-x[1][0], -x[1][1], x[0]))))
        r, c = key
        classroom[r][c] = cur_student
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if (0 <= nr < N and 0 <= nc < N) and classroom[nr][nc] == 0:
                possible_position[cur_student].add((nr, nc))

    else:
        r, c = search_blank()
        if (r, c) != (-1, -1):
            classroom[r][c] = cur_student
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if (0 <= nr < N and 0 <= nc < N) and classroom[nr][nc] == 0:
                    possible_position[cur_student].add((nr, nc))

answer = 0
score = [0, 1, 10, 100, 1000]
for r in range(N):
    for c in range(N):
        preference = student_info[classroom[r][c]]
        cnt = 0
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0 <= nr < N and 0 <= nc < N:
                if classroom[nr][nc] in preference:
                    cnt += 1

        answer += score[cnt]

print(answer)