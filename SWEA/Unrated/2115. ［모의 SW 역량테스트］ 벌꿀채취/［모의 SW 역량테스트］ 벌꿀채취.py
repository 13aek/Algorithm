from itertools import combinations

# 채취할 수 있는 벌꿀 찾기
def find_honey(arr):
    """
    각 일꾼이 각 구역에서 채취할 수 있는 최대 이익 계산하는 함수
    arr: honeys 벌통
    """
    # 각 구역에서의 최대 이익을 담을 리스트
    profit_list = []
    
    # 벌통을 순회
    for r in range(N):
        for c in range(N - M + 1):  # M개의 마스크로 순회하므로 범위 설정
            for i in range(1, M + 1):   # 1 ~ M 개 만큼의 조합의 수를 만들기 위해 범위 설정
                # 해당 위치의 이익 초기값
                profit = 0
                # 현재 마스크에서 나올 수 있는 조합을 순회
                for comb in combinations(arr[r][c:c + M], i):
                    # 최대 양보다 조합의 합이 크면
                    if C - sum(comb) < 0:
                        continue    # 다음 조합으로
                    # 조합의 합이 최대양과 같거나 작으면
                    else:
                        # 현재 조합의 이익 초기값
                        current_profit = 0
                        # 조합을 순회
                        for com in comb:
                            # 이익을 계산
                            current_profit += com**2
                        # 이익 중 가장 큰 이익 값으로 초기화
                        profit = max(profit, current_profit)
                
                # 리스트에 현재 행, 마스크의 열, 이익 을 담아줌
                profit_list += [[r, list(range(c, c+M)), profit]]
    
    # 이익 순으로 역정렬
    profit_list.sort(key=lambda x: x[2], reverse=True)
    
    return profit_list


def calc_max(arr):
    """
    이익 리스트를 인자로 받아 최대 이익을 계산하는 함수
    arr: profit_list
    """
    # 최대 이익 초기값
    max_profit = 0
    # 이익 리스트 중 2개를 뽑는 조합을 순회
    for comb in combinations(list(range(len(arr))), 2):
        # 해당 인덱스를 i, j에 부여
        i, j = comb[0], comb[1]
        # 뽑힌 조합들의 열의 교집합
        intersection = list(set(arr[i][1]) & set(arr[j][1]))
        # 만약 뽑힌 조합들의 행이 같고
        if arr[i][0] == arr[j][0]:
            # 교집합이 없다면
            if not intersection:
                # 맥스값 비교 후 업데이트
                max_profit = max(max_profit, arr[i][2] + arr[j][2])
        # 행이 안같으면
        else:
            # 맥스 값 비교 후 업데이트
            max_profit = max(max_profit, arr[i][2] + arr[j][2])

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