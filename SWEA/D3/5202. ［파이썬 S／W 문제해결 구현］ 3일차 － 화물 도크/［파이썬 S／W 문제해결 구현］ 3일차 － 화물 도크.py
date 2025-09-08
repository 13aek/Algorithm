T = int(input())

for tc in range(1, T+1):
    N = int(input())
    working_time = [list(map(int, input().split())) for _ in range(N)]

    working_time.sort(key=lambda x: x[1])
    count = 1
    cur_work = working_time[0]
    for i in range(1, N):
        if cur_work[1] <= working_time[i][0]:
            count += 1
            cur_work = working_time[i]

    print(f"#{tc} {count}")