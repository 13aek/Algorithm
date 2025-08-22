import sys
import itertools
from copy import deepcopy


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
    enemy_position = sorted(find_enemy(arr))[::-1]
    attack_enemy_positions = []
    for c in range(M):
        if arr[N][c] == 2:
            x, y = -1, -1
            min_dis = float("inf")
            for i in enemy_position:
                if distance(N, c, i[0], i[1]) < min_dis and distance(N, c, i[0], i[1]) <= d:
                    min_dis = distance(N, c, i[0], i[1])
                    x, y = i[0], i[1]
                elif distance(N, c, i[0], i[1]) == min_dis and distance(N, c, i[0], i[1]) <= d:
                    if y > i[1]:
                        x, y = i[0], i[1]
            if (x >= 0 and y >= 0) and [x, y] not in attack_enemy_positions:
                attack_enemy_positions += [[x, y]]

    for position in attack_enemy_positions:
        arr[position[0]][position[1]] = 0

    return arr


# 궁수를 성벽에 배치하는 함수
def place_archer(arr, c):
    for i in c:
        arr[-1][i] = 2
    return arr


# 디펜스 게임이 종료 될때까지 진행하는 함수
def play(arr, c):
    n = len(find_enemy(arr))
    eliminate_enemy_count = 0
    attack = attack_enemy(arr, D)
    eliminate_enemy_count += (n - len(find_enemy(attack)))
    next_turn = end_turn(attack)

    if len(find_enemy(next_turn)):
        return eliminate_enemy_count + play(next_turn, c)

    return eliminate_enemy_count


# sys.stdin = open('input.txt')

N, M, D = map(int, sys.stdin.readline().strip().split())
grid = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
castle = [[3] * M]

enemy_count = len(find_enemy(grid))

combs = list(itertools.combinations(list(range(M)), 3))

max_eliminate_enemy_count = 0
for comb in combs:
    total_grid = deepcopy(grid) + deepcopy(castle)
    game_grid = place_archer(total_grid, comb)
    cnt = play(game_grid, comb)
    max_eliminate_enemy_count = max(max_eliminate_enemy_count, cnt)
    if max_eliminate_enemy_count == enemy_count:
        break

print(max_eliminate_enemy_count)