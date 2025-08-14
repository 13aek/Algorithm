T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))

    sorted_scores = sorted(scores, reverse=True)

    max_sum = sum(sorted_scores[0:K])

    print(f"#{tc} {max_sum}")