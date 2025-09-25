import sys
from collections import deque
line = sys.stdin.readline


def is_rotated(rotate_magnetic, rotate_direction):
    """
    자석 회전 시키는 함수
    rotate_magnetic == 회전시킨 자석
    rotate_direction == 회전시킬 방향
    """
    check = [False] * 4     # 4개의 자석이 회전했는지 여부 체크
    q = deque()
    q.append((rotate_magnetic, rotate_direction))   # 처음 회전시킬 자석과 방향을 큐에 담음
    rotate_cmd = []
    while q:
        m, d = q.popleft()      # m = 자석, d = 방향

        # 이미 회전시켰으면 넘김
        if check[m]:
            continue

        check[m] = True     # 회전 체크
        rotate_cmd.append((m, d))

        # 인접한 자석 체크
        for nm in adj_list[m]:
            # 아직 회전 안했을 때
            if not check[nm]:
                # 1. 현재 자석의 왼쪽에 위치하고 인접한 자석의 극이 다르면 큐에 담음
                if nm < m and magnetic_field[nm][2] != magnetic_field[m][6]:
                    q.append((nm, -d))
                # 2. 현재 자석의 오른쪽에 위치하고, 인접한 자석의 극이 다르면 큐에 담음
                elif nm > m and magnetic_field[nm][6] != magnetic_field[m][2]:
                    q.append((nm, -d))

    for m, d in rotate_cmd:
        magnetic_field[m].rotate(d)


# 회전시키기 위해서 입력을 deque 으로 받음
magnetic_field = [deque(list(map(int, line().strip()))) for _ in range(4)]
K = int(line())
rotate_info = [list(map(int, line().split())) for _ in range(K)]

adj_list = [[1], [0, 2], [1, 3], [2]]     # 인접한 자석 리스트 만들어줌

for i in range(K):
    rm, rd = rotate_info[i]     # rm: 회전시킬 자석, rd: 방향
    is_rotated(rm - 1, rd)      # 자석 번호는 index 로 바꿔서 함수 호출

score = [1, 2, 4, 8]    # 자석마다 점수 배점
total_score = 0
for i in range(4):
    total_score += (score[i] * magnetic_field[i][0])

print(total_score)