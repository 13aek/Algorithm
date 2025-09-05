from itertools import combinations

# 채취할 수 있는 벌꿀 찾기
def find_honey(arr):
    """
    각 일꾼이 각 구역에서 채취할 수 있는 최대 이익 계산하는 함수
    arr: honeys 벌통
    """
    # 각 구역에서의 최대 이익을 담을 리스트
    profit_list = [[0] * N for _ in range(N)]

    # 벌통을 순회
    for r in range(N):
        for c in range(N - M + 1):  # M개의 마스크로 순회하므로 범위 설정

            # 현재 마스크의 합이 C보다 작거나 같으면 최대 이익 리스트에 담아줌
            if sum(arr[r][c:c + M]) <= C:
                profit_list[r][c] = sum(i * i for i in arr[r][c:c + M])
                continue

            else:
                for i in range(1, M):   # 1 ~ M 개 만큼의 조합의 수를 만들기 위해 범위 설정
                    # 해당 위치의 이익 초기값
                    profit = 0

                    # 현재 마스크에서 나올 수 있는 조합을 순회
                    for comb in combinations(arr[r][c:c + M], i):
                        # 최대 양보다 조합의 합이 크면 다음 조합으로
                        if C - sum(comb) < 0:
                            continue
                        # 현재 조합 중 가장 큰 값으로 profit 초기화
                        else:
                            current_profit = 0
                            for com in comb:
                                current_profit += com**2
                            profit = max(profit, current_profit)

                    # 만약 현재 위치의 이익보다 크면 갱신
                    if profit > profit_list[r][c]:
                        profit_list[r][c] = profit

    return profit_list


def calc_max(arr):
    """
    이익 리스트를 인자로 받아 최대 이익을 계산하는 함수
    arr: profit_list
    """

    if M * 2 > len(arr):
        pl = []
        for r in range(N):
            pl += [max(arr[r])]
        pl.sort(reverse=True)
        return pl[0] + pl[1]
    else:
        max_profit = 0
        for r in range(N):
            for c in range(N-M+1):
                pr1 = arr[r][c]
                for rr in range(r, N):

                    pr1_c = 0
                    
                    if rr == r:
                        pr1_c = c + M

                    for cc in range(pr1_c, N-M+1):
                        pr2 = arr[rr][cc]
                        if pr1 + pr2 > max_profit:
                            max_profit = pr1 + pr2
        return max_profit


T = int(input())

for tc in range(1, T+1):
    # N: 벌통의 크기, M: 선택할 수 있는 벌통의 개수, C: 최대 양
    N, M, C = map(int, input().split())
    # honeys: 벌통
    honeys = [list(map(int, input().split())) for _ in range(N)]

    # 각 일꾼이 수익을 얻을 수 있는 모든 경우의 수를 받음
    p_list = find_honey(honeys)
    # p_list 에서 두 일꾼이 얻을 수 있는 최대 수익을 계산
    result = calc_max(p_list)

    print(f"#{tc} {result}")
