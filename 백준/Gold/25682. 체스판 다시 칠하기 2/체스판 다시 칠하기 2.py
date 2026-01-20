# BOJ Gold 4 25682_체스판 다시 칠하기 2

import sys
input = sys.stdin.readline

# N: 행, M: 열, K: 부분 정사각형 크기
N, M, K = map(int, input().split())

# 보드 입력
board = [input().strip() for _ in range(N)]

# 2D prefix sum P (N+1 x M+1)
# P[i+1][j+1] = (0,0)~(i,j)까지 'W 시작 체스패턴'과 다른 칸 수 누적합
P = [[0] * (M + 1) for _ in range(N + 1)]

# prefix sum 생성
for i in range(N):
    # i번째 줄 문자열
    row = board[i]
    # 현재 행에서 (i,0)~(i,j) mismatch 누적합
    row_sum = 0
    # P의 위쪽 행 참조
    Pi = P[i]
    # P의 현재 행(채울 행) 참조
    Pn = P[i + 1]

    for j in range(M):
        # (i+j) 짝수면 기대값 W, 홀수면 B
        # 기대값과 다르면 mismatch=1
        if ((i + j) & 1) == 0:
            mismatch = 1 if row[j] != 'W' else 0
        else:
            mismatch = 1 if row[j] != 'B' else 0

        # 행 누적합 갱신
        row_sum += mismatch
        # 2D prefix 갱신: 위쪽 누적(Pi[j+1]) + 현재행 누적(row_sum)
        Pn[j + 1] = Pi[j + 1] + row_sum

# 정답 초기화
ans = 10**18

# 자주 쓰는 값 로컬 변수로 캐싱
KK = K * K
P_local = P  # 전역 이름 접근보다 로컬이 빠름

# 모든 KxK 구간 탐색
for i in range(N - K + 1):
    # 사각형 계산에 필요한 위/아래 prefix 행을 미리 잡음
    top = P_local[i]
    bottom = P_local[i + K]
    for j in range(M - K + 1):
        # (i,j)~(i+K-1,j+K-1) mismatch 합
        # = bottom[j+K] - top[j+K] - bottom[j] + top[j]
        w_need = bottom[j + K] - top[j + K] - bottom[j] + top[j]
        # B 시작 패턴은 반대이므로 K*K - w_need
        b_need = KK - w_need
        # 최소 갱신
        if w_need < ans:
            ans = w_need
        if b_need < ans:
            ans = b_need

print(ans)