def dfs(cur_fee, cur_idx):
    global min_fee

    # 종료 조건
    # 1. cur_idx 가 11보다 크면
    if cur_idx > 11:
        # cur_fee 가 min_fee 보다 작으면 갱신
        if cur_fee < min_fee:
            min_fee = cur_fee
        return

    # 2. cur_fee 가 min_fee 보다 커지면
    if cur_fee >= min_fee:
        return

    # plan[cur_idx] 가 0이면 다음달로
    if plan[cur_idx] == 0:
        dfs(cur_fee, cur_idx + 1)

    # 1일권
    dfs(cur_fee + fee[0] * plan[cur_idx], cur_idx + 1)
    # 1달권
    dfs(cur_fee + fee[1], cur_idx + 1)
    # 3달권
    dfs(cur_fee + fee[2], cur_idx + 3)
    # 1년권
    dfs(cur_fee + fee[3], cur_idx + 12)


T = int(input())

for tc in range(1, T + 1):
    # 1일 요금, 1달 요금, 3달 요금, 1년 요금
    fee = list(map(int, input().split()))
    # 12개월 이용 계획
    plan = list(map(int, input().split()))

    min_fee = float('inf')

    dfs(0, 0)

    print(f"#{tc} {min_fee}")