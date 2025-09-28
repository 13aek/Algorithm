from heapq import heappush, heappop, heapify


def solution(scoville, K):
    answer = 0

    def scoville_score(k1, k2):
        return k1 + (k2 * 2)

    heapify(scoville)

    while scoville:
        first = heappop(scoville)

        if first >= K:
            break

        if not scoville:
            answer = -1
            break

        second = heappop(scoville)

        mixed = scoville_score(first, second)
        answer += 1
        heappush(scoville, mixed)

    return answer
