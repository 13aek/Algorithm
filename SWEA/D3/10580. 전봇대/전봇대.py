T = int(input())
for tc in range(1, T+1):
    N = int(input())
    line = []
    left_cross = []
    right_cross = []

    for _ in range(N):
        Ai, Bi = map(int, input().split())
        if Ai == Bi:
            line.append(Ai)
        else:
            left_cross.append(Ai)
            right_cross.append(Bi)

    cross_point = 0
    for i in range(len(left_cross)):
        if left_cross[i] < right_cross[i]:
            for j in line:
                if j in range(left_cross[i], right_cross[i] + 1):
                    cross_point += 1
        else:
            for j in line:
                if j in range(right_cross[i], left_cross[i] + 1):
                    cross_point += 1

    for i in range(len(right_cross) - 1):
        for j in range(i + 1, len(right_cross)):
            if left_cross[i] < left_cross[j] and right_cross[i] > right_cross[j]:
                cross_point += 1
            elif left_cross[i] > left_cross[j] and right_cross[i] < right_cross[j]:
                cross_point += 1

    print(f"#{tc} {cross_point}")