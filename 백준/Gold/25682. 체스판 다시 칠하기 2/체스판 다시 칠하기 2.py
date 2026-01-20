# BOJ Gold 4 25682_체스판 다시 칠하기 2

import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [input().strip() for _ in range(N)]

# mismatchW[i][j] = (i,j)가 'W로 시작하는 체스판' 기대값과 다르면 1, 아니면 0
mismatchW = [[0] * M for _ in range(N)]

# mismatch 배열 채우기
for i in range(N):
    for j in range(M):
        # W 시작 패턴에서 (i+j)가 짝수면 W, 홀수면 B가 기대값
        expected = 'W' if (i + j) % 2 == 0 else 'B'
        # 실제와 기대가 다르면 1, 같으면 0
        mismatchW[i][j] = 1 if board[i][j] != expected else 0

# 2D prefix sum P 만들기 (크기를 (N+1)x(M+1)로 해서 경계 처리)
P = [[0] * (M + 1) for _ in range(N + 1)]

# P[i+1][j+1]에 (0,0)~(i,j)까지 mismatchW 합 저장
for i in range(N):
    row_sum = 0  # 현재 행에서 (i,0)~(i,j) 누적합
    for j in range(M):
        row_sum += mismatchW[i][j]              # 행 누적합 갱신
        P[i + 1][j + 1] = P[i][j + 1] + row_sum # 위쪽 누적 + 현재행 누적

# prefix sum으로 (x1,y1)~(x2,y2) 구간 합 구하는 함수
def rect_sum(x1, y1, x2, y2):
    # prefix 인덱스는 +1 보정
    return (
        P[x2 + 1][y2 + 1]
        - P[x1][y2 + 1]
        - P[x2 + 1][y1]
        + P[x1][y1]
    )

ans = 10**18

# 모든 KxK 구간의 좌상단 (i,j)을 순회
for i in range(N - K + 1):
    for j in range(M - K + 1):
        # 해당 구간이 W 시작 패턴과 다른 칸 수
        w_need = rect_sum(i, j, i + K - 1, j + K - 1)
        # B 시작 패턴은 완전히 반대이므로 K*K - w_need
        b_need = K * K - w_need
        # 둘 중 최소로 답 갱신
        ans = min(ans, w_need, b_need)

print(ans)
