# [Gold III] 캐슬 디펜스 - 17135 

[문제 링크](https://www.acmicpc.net/problem/17135) 

### 성능 요약

메모리: 32412 KB, 시간: 436 ms

### 풀이 방법

완전 탐색 방법 사용 / 다른 방법으로 풀이도 시도하는게 좋을 것 같음.. 

### 분류

구현, 그래프 이론, 브루트포스 알고리즘, 그래프 탐색, 시뮬레이션, 너비 우선 탐색

### 제출 일자

2025년 8월 22일 12:19:42

### 문제 설명

<p>캐슬 디펜스는 성을 향해 몰려오는 적을 잡는 턴 방식의 게임이다. 게임이 진행되는 곳은 크기가 N×M인 격자판으로 나타낼 수 있다. 격자판은 1×1 크기의 칸으로 나누어져 있고, 각 칸에 포함된 적의 수는 최대 하나이다. 격자판의 N번행의 바로 아래(N+1번 행)의 모든 칸에는 성이 있다.</p>

<p>성을 적에게서 지키기 위해 궁수 3명을 배치하려고 한다. 궁수는 성이 있는 칸에 배치할 수 있고, 하나의 칸에는 최대 1명의 궁수만 있을 수 있다. 각각의 턴마다 궁수는 적 하나를 공격할 수 있고, 모든 궁수는 동시에 공격한다. 궁수가 공격하는 적은 거리가 D이하인 적 중에서 가장 가까운 적이고, 그러한 적이 여럿일 경우에는 가장 왼쪽에 있는 적을 공격한다. 같은 적이 여러 궁수에게 공격당할 수 있다. 공격받은 적은 게임에서 제외된다. 궁수의 공격이 끝나면, 적이 이동한다. 적은 아래로 한 칸 이동하며, 성이 있는 칸으로 이동한 경우에는 게임에서 제외된다. 모든 적이 격자판에서 제외되면 게임이 끝난다. </p>

<p>게임 설명에서 보다시피 궁수를 배치한 이후의 게임 진행은 정해져있다. 따라서, 이 게임은 궁수의 위치가 중요하다. 격자판의 상태가 주어졌을 때, 궁수의 공격으로 제거할 수 있는 적의 최대 수를 계산해보자.</p>

<p>격자판의 두 위치 (r<sub>1</sub>, c<sub>1</sub>), (r<sub>2</sub>, c<sub>2</sub>)의 거리는 |r<sub>1</sub>-r<sub>2</sub>| + |c<sub>1</sub>-c<sub>2</sub>|이다.</p>

### 입력 

 <p>첫째 줄에 격자판 행의 수 N, 열의 수 M, 궁수의 공격 거리 제한 D가 주어진다. 둘째 줄부터 N개의 줄에는 격자판의 상태가 주어진다. 0은 빈 칸, 1은 적이 있는 칸이다.</p>

### 출력 

 <p>첫째 줄에 궁수의 공격으로 제거할 수 있는 적의 최대 수를 출력한다.</p>

### 제출 이력

| 제출 번호 | 아이디     | 문제  | 결과                            | 메모리(KB) | 시간(ms) | 언어            | 코드 길이 | 제출한 시간 |
|---------:|:----------:|:-----:|:--------------------------------|-----------:|---------:|:----------------|----------:|:-----------:|
| 97718587 | baekus2209 | 17135 | 맞았습니다!!                    |     32412  |     436  | Python 3 / 수정 |     2406  |   1분 전    |
| 97717507 | baekus2209 | 17135 | 맞았습니다!!                    |     33884  |    1068  | Python 3 / 수정 |     2735  |  48분 전    |
| 97717484 | baekus2209 | 17135 | 런타임 에러 (FileNotFoundError) |       -    |     -    | Python 3 / 수정 |     2733  |  48분 전    |
| 97715945 | baekus2209 | 17135 | 틀렸습니다                       |       -    |     -    | Python 3 / 수정 |     2497  |  1시간 전   |
| 97715565 | baekus2209 | 17135 | 시간 초과                        |       -    |     -    | Python 3 / 수정 |     2497  |  1시간 전   |
| 97715380 | baekus2209 | 17135 | 런타임 에러 (ValueError)        |       -    |     -    | Python 3 / 수정 |     2491  |  2시간 전   |
| 97715226 | baekus2209 | 17135 | 런타임 에러 (ValueError)        |       -    |     -    | Python 3 / 수정 |     2735  |  2시간 전   |

- 런타임 에러는 백준 입력 방식을 못지켜서..
- 제대로된 제출은 시간 초과 -> 틀렸습니다 -> 맞았습니다 순서
- 맨 처음 맞춘 코드는 아래 첨부
- 지금 올라간 .py는 제 코드 gpt 도움 받아서 최적화 시킨 것 (시간 부분 2배 이상 최적화 됨)

<br>

```python
# 두 격자판의 거리를 계산하는 함수
def distance(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)


# 궁수가 공격이 가능한 좌표 값을 반환하는 함수
def possible_attack(arr, row, col, d):
    possible = []
    for r in range(N+1):
        for c in range(M):
            if distance(row, col, r, c) <= d:
                possible += [[r, c]]
    return possible


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


# 격자판에 궁수 3명을 배치할 수 있는 좌표 값 반환
def possible_place(arr, d):
    # 처음 배치일 때 공격 가능 거리에 적이 없으면 배치 x
    enemy_position = set(map(tuple, find_enemy(arr)))
    possible = []
    for r in range(N+1):
        for c in range(M):
            if arr[r][c] != 1:
                if set(map(tuple, possible_attack(arr, r, c, d))) & enemy_position:
                    possible += [[r, c]]

    if not possible:
        return possible_place(end_turn(arr), d)

    return possible


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


T = int(input())

for tc in range(1, T+1):
    N, M, D = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
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
```
