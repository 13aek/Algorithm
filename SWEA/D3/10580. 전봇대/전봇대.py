T = int(input())
for tc in range(1, T+1):
    N = int(input())
    wires = [list(map(int, input().split())) for _ in range(N)]
    # 교차점 기록
    cross_point = 0

    for i, (a, b) in enumerate(wires):
        for c, d in wires[i:]:
            if a > c and b < d:
                cross_point += 1
            elif a < c and b > d:
                cross_point += 1

    print(f"#{tc} {cross_point}")