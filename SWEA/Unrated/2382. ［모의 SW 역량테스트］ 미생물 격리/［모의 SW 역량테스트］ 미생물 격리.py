# 델타 방향 (상하좌우)
drc = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}

# 반대 방향 회전
rotate_direction = {1: 2, 2: 1, 3: 4, 4: 3}


def simulate(micro):
    time = 0

    while micro:
        if time == M:
            break

        bucket = {}

        for (r, c), (cnt, d, _) in micro.items():
            nr, nc = r + drc[d][0], c + drc[d][1]
            new_cnt = cnt
            nd = d

            if nr == 0 or nr == N - 1 or nc == 0 or nc == N - 1:
                new_cnt = cnt // 2
                nd = rotate_direction[d]

            if new_cnt == 0:
                continue

            if (nr, nc) in bucket:
                if new_cnt > bucket[(nr, nc)][2]:
                    sum_d = nd
                    compare_cnt = new_cnt
                else:
                    sum_d = bucket[(nr, nc)][1]
                    compare_cnt = bucket[(nr, nc)][2]

                sum_cnt = new_cnt + bucket[(nr, nc)][0]
                bucket[(nr, nc)] = [sum_cnt, sum_d, compare_cnt]
            else:
                bucket[(nr, nc)] = [new_cnt, nd, new_cnt]

        time += 1
        micro = bucket

    micro_count = 0
    for count, _, _ in micro.values():
        micro_count += count

    return micro_count


for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    microbial_community = {}
    for _ in range(K):
        pr, pc, n, direction = map(int, input().split())
        microbial_community[(pr, pc)] = [n, direction, n]

    result = simulate(microbial_community)
    print(f"#{tc} {result}")