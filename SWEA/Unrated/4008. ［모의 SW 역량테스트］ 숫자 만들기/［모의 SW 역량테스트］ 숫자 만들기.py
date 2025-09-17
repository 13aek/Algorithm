def dfs(i, total, plus, minus, mul, div):
    global min_result, max_result

    # 모든 숫자를 다 사용했다면
    if i == N - 1:
        # 최종 결과로 최소값, 최대값 갱신
        min_result = min(min_result, total)
        max_result = max(max_result, total)
        return
    
    # plus 횟수가 남아있을때
    if plus > 0:
        dfs(i + 1, total + numbers[i + 1], plus - 1, minus, mul, div)
    # minus 횟수가 남아있을때
    if minus > 0:
        dfs(i + 1, total - numbers[i + 1], plus, minus - 1, mul, div)
    # mul 횟수가 남아있을때
    if mul > 0:
        dfs(i + 1, total * numbers[i + 1], plus, minus, mul - 1, div)
    # div 횟수가 남아있을때
    if div > 0:
        dfs(i + 1, int(total / numbers[i + 1]), plus, minus, mul, div - 1)


for tc in range(1, int(input()) + 1):
    N = int(input())
    operators = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    min_result = 1e9
    max_result = -1e9

    dfs(0, numbers[0], operators[0], operators[1], operators[2], operators[3])

    print(f"#{tc} {max_result - min_result}")