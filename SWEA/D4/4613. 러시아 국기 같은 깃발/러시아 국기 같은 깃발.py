T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    flag = [list(input()) for _ in range(N)]

    flag_cnt = [[0] * 3 for _ in range(N)]

    # 처음 색칠한 횟수 저장
    result = 0

    # 맨 윗 줄과 맨 아래줄은 일단 W 랑 R 로 채우고
    result += flag[0].count('R') + flag[0].count('B')
    result += flag[-1].count('W') + flag[-1].count('B')

    # 각 행에 본인 색 외에 칠해야할 색들의 개수들의 누적합을 구함
    w_cnt, b_cnt, r_cnt = 0, 0, 0
    for r in range(1, N-1):
        w_cnt += flag[r].count('B') + flag[r].count('R')
        b_cnt += flag[r].count('W') + flag[r].count('R')
        r_cnt += flag[r].count('W') + flag[r].count('B')
        flag_cnt[r] = [w_cnt, b_cnt, r_cnt]

    # 최소값을 저장할 초기값
    min_cnt = N * M
    
    # 흰색을 0 ~ i, 블루를 i+1 ~ j, 레드를 j+1 ~ N-1 까지 칠할 경우
    for i in range(N-2):
        for j in range(i+1, N-1):
            cnt = flag_cnt[i][0]\
                  + (flag_cnt[j][1] - flag_cnt[i][1])\
                  + (flag_cnt[N-2][2] - flag_cnt[j][2])
            min_cnt = min(min_cnt, cnt)

    print(f"#{tc} {min_cnt + result}")