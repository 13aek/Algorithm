import sys
import itertools

# sys.stdin = open('input.txt')


# 두 격자판의 거리를 계산하는 함수
def distance(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)


# 적이 위치한 좌표값을 반환하는 함수
def find_enemy(arr):
    enemy_position = []
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 1:
                enemy_position += [[r, c]]
    return enemy_position


# 턴이 끝났을 때 적이 이동하고 난 후 좌표값을 반환하는 함수
def end_turn(arr):
    move = [[0] * M]
    move_arr = move + arr[:N-1]
    return move_arr + [arr[-1]]


# 궁수가 해당 턴에 적을 공격해서 제거한 수를 반환하는 함수
# 한 턴에 동시 공격이 가능함..
def attack_enemy(arr, d):
    enemy_position = find_enemy(arr)    # 변경
    targets = set()  # (r, c) 튜플로 중복 방지

    for c in range(M):
        if arr[N][c] == 2:
            x, y = -1, -1
            min_dis = float("inf")
            for er, ec in enemy_position:
                dist = distance(N, c, er, ec)
                if dist <= d:
                    if dist < min_dis or (dist == min_dis and ec < y):
                        min_dis = dist
                        x, y = er, ec

            if x >= 0:
                targets.add((x, y))

    killed = 0
    for r, c in targets:
        if arr[r][c] == 1:
            arr[r][c] = 0
            killed += 1

    return arr, killed


# 궁수를 성벽에 배치하는 함수
def place_archer(arr, c):
    for i in c:
        arr[-1][i] = 2
    return arr


# 디펜스 게임이 종료 될때까지 진행하는 함수
def play(arr, c):
    if not find_enemy(arr):
        return 0

    attack, killed = attack_enemy(arr, D)
    next_turn = end_turn(attack)

    return killed + play(next_turn, c)


N, M, D = map(int, sys.stdin.readline().strip().split())
grid = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
castle = [[3] * M]

enemy_count = len(find_enemy(grid))

max_eliminate_enemy_count = 0
for comb in itertools.combinations(list(range(M)), 3):
    total_grid = [row[:] for row in grid] + [castle[0][:]]
    game_grid = place_archer(total_grid, comb)
    cnt = play(game_grid, comb)
    max_eliminate_enemy_count = max(max_eliminate_enemy_count, cnt)
    if max_eliminate_enemy_count == enemy_count:
        break

print(max_eliminate_enemy_count)