import sys
line = sys.stdin.readline


# 색종이 붙이는 함수
def is_colored(array, cur_r, cur_c, size):
    if 0 <= cur_r + size <= 10 and 0 <= cur_c + size <= 10:
        mask = [row[cur_c:cur_c+size] for row in array[cur_r:cur_r+size]]
        for m in mask:
            if 0 in m:
                break
        else:
            return True

    return False


def restore(arr, cur_r, cur_c, size, num):
    for r1 in range(cur_r, cur_r + size):
        for c1 in range(cur_c, cur_c + size):
            arr[r1][c1] = num


# 종이 붙이는 경우를 백트래킹
def backtrack(arr, cur_cnt, one_cnt, one, two, three, four, five):
    global min_cnt
    max_cover = one * 1 * 1 + two * 2 * 2 + three * 3 * 3 + four * 4 * 4 + five * 5 * 5
    # 조기 종료 조건
    # 1. 현재 종이 붙인 횟수가 기록된 최소 붙인 횟수보다 크거나 같을 때
    if min_cnt <= cur_cnt:
        return

    # 2. 색종이가 다 떨어졌는데 아직 1이 남아있을때
    if sum([one, two, three, four, five]) == 0 and one_cnt:
        return

    # 3. 남은 1의 개수가 현재 보유 색종이로 덮을 수 있는 최대 면적보다 크면 종료
    if max_cover < one_cnt:
        return

    # 종료 조건
    # 1. 종이에 1이 더이상 남아있지 않을 때
    if not one_cnt:
        min_cnt = min(min_cnt, cur_cnt)
        return

    for r in range(10):
        for c in range(10):
            if arr[r][c] == 1:
                if five > 0 and is_colored(arr, r, c, 5):
                    restore(arr, r, c, 5, 0)
                    new_one_cnt = one_cnt - 5 * 5
                    backtrack(arr, cur_cnt + 1, new_one_cnt, one, two, three, four, five - 1)
                    restore(arr, r, c, 5, 1)

                if four > 0 and is_colored(arr, r, c, 4):
                    restore(arr, r, c, 4, 0)
                    new_one_cnt = one_cnt - 4 * 4
                    backtrack(arr, cur_cnt + 1, new_one_cnt, one, two, three, four - 1, five)
                    restore(arr, r, c, 4, 1)

                if three > 0 and is_colored(arr, r, c, 3):
                    restore(arr, r, c, 3, 0)
                    new_one_cnt = one_cnt - 3 * 3
                    backtrack(arr, cur_cnt + 1, new_one_cnt, one, two, three - 1, four, five)
                    restore(arr, r, c, 3, 1)

                if two > 0 and is_colored(arr, r, c, 2):
                    restore(arr, r, c, 2, 0)
                    new_one_cnt = one_cnt - 2 * 2
                    backtrack(arr, cur_cnt + 1, new_one_cnt, one, two - 1, three, four, five)
                    restore(arr, r, c, 2, 1)

                if one > 0 and is_colored(arr, r, c, 1):
                    restore(arr, r, c, 1, 0)
                    new_one_cnt = one_cnt - 1 * 1
                    backtrack(arr, cur_cnt + 1, new_one_cnt, one - 1, two, three, four, five)
                    restore(arr, r, c, 1, 1)

                return

paper = [list(map(int, line().split())) for _ in range(10)]
one_count = 0
for r in range(10):
    for c in range(10):
        if paper[r][c] == 1:
            one_count += 1
min_cnt = float('inf')

backtrack(paper, 0, one_count, 5, 5, 5, 5, 5)

print(-1 if min_cnt == float('inf') else min_cnt)