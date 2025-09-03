from copy import deepcopy


# 합격 여부 판단하는 함수
def is_pass(film):
    for c in range(W):
        streak = 1
        ok = False
        for r in range(1, D):
            if film[r][c] == film[r-1][c]:
                streak += 1
                if streak >= K:
                    ok = True
                    break
            else:
                streak = 1

        if not ok:
            return False

    return True


def min_injection_dfs(film, d, cnt):
    global min_cnt

    if K == 1:
        min_cnt = 0
        return

    # 종료 조건 1
    if cnt >= min_cnt:
        return

    # 종료 조건 2
    if cnt >= K:
        return

    # 종료 조건 3
    if d == D:
        if is_pass(film):
            min_cnt = min(min_cnt, cnt)
            return
        else:
            return

    # 1. d행을 변경하지 않음
    film[d] = protect_film[d]
    min_injection_dfs(film, d + 1, cnt)

    # 2. d행에 A 시약 투여
    film[d] = A
    min_injection_dfs(film, d + 1, cnt + 1)

    # 3. d행에 B 시약 투여
    film[d] = B
    min_injection_dfs(film, d + 1, cnt + 1)


T = int(input())

for tc in range(1, T+1):
    D, W, K = map(int, input().split())
    protect_film = [list(map(int, input().split())) for _ in range(D)]
    protect_film_copy = deepcopy(protect_film)
    A, B = [0] * W, [1] * W
    cnt = 0
    min_cnt = K
    min_injection_dfs(protect_film_copy, 0, cnt)
    print(f"#{tc} {min_cnt}")



