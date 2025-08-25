# 이미 저장한 서브 매트릭스 행렬을 0으로 바꾸는 함수 정의
def change_zero(arr, start_row, start_col, last_row, last_col):
    for a in range(start_row, last_row):
        for b in range(start_col, last_col):
            arr[a][b] = 0
    return arr


# 델타 방향 정의 (우, 하)
dr = [0, 1]
dc = [1, 0]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    chemicals = [list(map(int, input().split())) for _ in range(N)]

    sub_matrix = []
    # 행렬 순회하면서 화학 물질이 담긴 용기들 찾기
    for r in range(N):
        for c in range(N):
            if chemicals[r][c] != 0:
                x, y = 0, 0
                for i in range(2):
                    for j in range(N):
                        nr = r + dr[i] * j
                        nc = c + dc[i] * j

                        if 0 > nr or N <= nr or 0 > nc or N <= nc or chemicals[nr][nc] == 0 :
                            if i == 0:
                                y = nc
                                break
                            else:
                                x = nr
                                break
                sub_matrix += [[x-r, y-c, (x-r) * (y-c)]]
                chemicals = change_zero(chemicals, r, c, x, y)

    for i in range(len(sub_matrix)-1, -1, -1):
        for j in range(i):
            if sub_matrix[j][2] > sub_matrix[j+1][2]:
                sub_matrix[j], sub_matrix[j+1] = sub_matrix[j+1], sub_matrix[j]
            elif sub_matrix[j][2] == sub_matrix[j+1][2]:
                if sub_matrix[j][0] > sub_matrix[j+1][0]:
                    sub_matrix[j], sub_matrix[j + 1] = sub_matrix[j + 1], sub_matrix[j]

    print(f"#{tc} {len(sub_matrix)}", end=' ')
    for i in sub_matrix:
        print(*i[:2], end=' ')
    print()