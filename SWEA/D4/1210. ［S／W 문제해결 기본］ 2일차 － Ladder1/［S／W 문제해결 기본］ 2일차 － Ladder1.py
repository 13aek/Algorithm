# 델타 방향 정의 (좌, 우, 상)
dr = [0, 0, -1]
dc = [-1, 1, 0]

for tc in range(1, 11):
    '''
    도착지점에 도착하는 출발 지점 X의 좌표를 찾는 문제
    '''
    T = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    # 도착지점에서 역출발하기 위해 처음 위치 값 설정
    r = 99
    c = next(i for i in range(100) if ladder[99][i] == 2)

    # r > 0 보다 크면 반복하는 while 문 1
    while r > 0:
        # delta 방향으로 순회하는 for 문 1
        for i in range(3):
            nr = r + dr[i]      # row 좌표값 업데이트
            nc = c + dc[i]      # column 좌표값 업데이트

            if (0 <= nr < 100 and 0 <= nc < 100) and ladder[nr][nc] == 1:
                if i == 0 or i == 1:        # delta 방향이 좌 또는 우 일때

                    # ladder[nr][nc] 가 1이면 반복하는 while 문 2
                    while ladder[nr][nc] == 1:      # 1이 아닐 때까지 그 방향으로 직진
                        nc += dc[i]
                        if not 0 <= nc < 100:       # nc가 범위 안에 들어오지 않으면
                            break                   # while 문 2 중단

                    nc -= dc[i]     # 직진하던 반대 방향으로 한 칸 이동
                    nr -= 1         # 직진이 끝났으니 위로 한 칸 이동
                    r, c = nr, nc   # 좌표값 업데이트
                    break           # for 문 1 중단

                else:               # 델타 방향이 위일 경우
                    r, c = nr, nc   # 좌표값 업데이트
                    break           # for 문 1 중단

    print(f"#{tc} {c}")