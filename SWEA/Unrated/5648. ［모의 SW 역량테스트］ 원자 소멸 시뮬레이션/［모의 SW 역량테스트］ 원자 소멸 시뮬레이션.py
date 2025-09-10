# 델타 방향 정의 (상 하 좌 우)
drc = [(0, 1), (0, -1), (-1, 0), (1, 0)]


def simulate(atoms):
    total_energy = 0

    while atoms:
        bucket = {}

        for (x, y), (d, e) in atoms.items():
            nx = x + drc[d][0]
            ny = y + drc[d][1]

            if nx < -2000 or nx > 2000 or ny < -2000 or ny > 2000:
                continue

            if (nx, ny) in bucket:
                cnt, esum, sd, se = bucket[(nx, ny)]
                cnt += 1
                esum += e
                bucket[(nx, ny)] = [cnt, esum, sd, se]
            else:
                bucket[(nx, ny)] = [1, e, d, e]

        next_atoms = {}
        for (x, y), (cnt, esum, sd, se) in bucket.items():
            if cnt >= 2:
                total_energy += esum
            else:
                next_atoms[(x, y)] = (sd, se)

        atoms = next_atoms

    return total_energy


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    atomic_info = [list(map(int, input().split())) for _ in range(N)]

    power_plant = {}
    for a, b, d, c in atomic_info:
        power_plant[(a * 2, b * 2)] = (d, c)

    ans = simulate(power_plant)

    print(f"#{tc} {ans}")
