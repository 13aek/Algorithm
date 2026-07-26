def solution(n):
    answer = 0
    left, right = 1, 1
    total = 1

    while left <= n:
        if total == n:
            answer += 1
            total -= left
            left += 1
        elif total < n:
            right += 1
            total += right
        else:
            total -= left
            left += 1

    return answer