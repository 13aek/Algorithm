import sys

line = sys.stdin.readline

N = int(line())
dice = [list(map(int, line().split())) for _ in range(N)]

pair = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}

result = 0
first_dice = dice[0]

for i in range(6):
    idx = [0, 1, 2, 3, 4, 5]
    bottom = i
    top = pair[i]
    answer = max([first_dice[i] for i in idx if i != top and i != bottom])
    b_value = first_dice[bottom]
    t_value = first_dice[top]

    for j in range(1, N):
        next_dice = dice[j]
        bottom = next_dice.index(t_value)
        top = pair[bottom]
        answer += max([next_dice[i] for i in idx if i != top and i != bottom])
        b_value = next_dice[bottom]
        t_value = next_dice[top]

    result = max(result, answer)

print(result)