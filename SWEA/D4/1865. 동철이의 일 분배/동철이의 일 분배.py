def backtrack(arr, cur_r, cur_c, cur_percent):
    global max_percent

    # 종료 조건
    # 현재 행이 N 과 똑같아졌을때
    if cur_r == N - 1:
        if max_percent < cur_percent:
            max_percent = cur_percent
        return

    # 조기 종료 조건
    # 1. max_percent 보다 현재 percent 가 작거나 같을때
    if max_percent >= cur_percent:
        return
    # 2. 이미 기록된 col 일 경우
    if visited[cur_c]:
        return

    # 현재 열 방문 처리
    visited[cur_c] = True
    # 다음 직원으로
    nr = cur_r + 1

    # 공장 순회
    for nc in range(N):
        # 방문하지 않은 일이고 그 일의 확률이 0이 아니면
        if not visited[nc] and arr[nr][nc] != 0:
            # 현재 퍼센트 * 다음 퍼센트
            n_percent = cur_percent * (arr[nr][nc] / 100)

            # 백트랙 재귀
            backtrack(arr, nr, nc, n_percent)

            # 백트랙 후 방문 처리 취소
            visited[nc] = False


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    Pij = [list(map(int, input().split())) for _ in range(N)]

    max_percent = 0

    for c in range(N):
        if Pij[0][c] != 0:
            visited = [False] * N
            percent_c = Pij[0][c] / 100
            backtrack(Pij, 0, c, percent_c)

    print(f"#{tc} {(max_percent * 100):.6f}")