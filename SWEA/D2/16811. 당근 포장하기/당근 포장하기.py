from collections import Counter


def box_wrap():
    # 1. 사이즈별 빈도 계산
    freq = []
    cnt = Counter(ci)
    unique = sorted(cnt)
    for size in unique:
        if cnt[size] > N // 2:
            return -1
        freq.append(cnt[size])

    # 당근의 고유 사이즈가 3개 미만이면 나눠 담을 수 없음
    m = len(freq)
    if m < 3:
        return -1

    # 2. 누적합으로 구간 합 구함
    prefix_sum = [0] * (m + 1)
    for i in range(1, m + 1):
        prefix_sum[i] = prefix_sum[i-1] + freq[i - 1]

    def range_sum(l, r):
        if l > r:
            return 0
        return prefix_sum[r + 1] - prefix_sum[l]

    limit = N // 2
    result = None

    for i in range(0, m - 2):
        for j in range(i + 1, m - 1):
            A = range_sum(0, i)
            B = range_sum(i + 1, j)
            C = range_sum(j + 1, m -1)

            if not (1 <= A <= limit):
                continue
            if not (1 <= B <= limit):
                continue
            if not (1 <= C <= limit):
                continue

            diff = max(A, B, C) - min(A, B, C)

            if result is None or diff < result:
                result = diff

    return result if result is not None else - 1


for tc in range(1, int(input()) + 1):
    N = int(input())
    ci = list(map(int, input().split()))
    ci.sort()

    ans = box_wrap()
    print(f"#{tc} {ans}")