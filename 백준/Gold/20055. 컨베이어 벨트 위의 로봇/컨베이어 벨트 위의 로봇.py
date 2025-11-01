import sys
from collections import deque

# 입력 가속
input = sys.stdin.readline

# 단일 테스트 케이스 기준 (BOJ 20055)
N, K = map(int, input().split())           # N: 위쪽 벨트 칸 수, K: 내구도 0 칸 개수 기준
A = deque(map(int, input().split()))       # 길이 2N의 내구도 배열 (deque로 회전용)
robots = deque([False] * (2 * N))          # 각 칸에 로봇 존재 여부 (deque로 함께 회전)
steps = 0                                  # 정답: 몇 단계에서 종료되는지

while True:
    steps += 1                             # 단계 시작 → 단계 수 1 증가

    # 1) 벨트와 로봇을 함께 한 칸 회전
    A.rotate(1)                            # 내구도 배열을 오른쪽으로 1칸 회전
    robots.rotate(1)                       # 로봇 배열도 같은 방향으로 1칸 회전 (같은 칸을 가리키도록)
    robots[N - 1] = False                  # 내리는 위치(N-1)라서, 그 칸의 로봇은 즉시 내려야 함

    # 2) 로봇 이동: 뒤에서 앞으로 (N-2 → 0)
    #    - 앞 칸에 로봇이 없고, 앞 칸 내구도 > 0 이면 한 칸 이동
    for i in range(N - 2, -1, -1):         # 올리는 위치 0 ~ 내리는 위치 직전 N-2까지 역순
        if robots[i] and not robots[i + 1] and A[i + 1] > 0:
            robots[i] = False              # 현재 칸의 로봇 이동 시작 (떠남)
            robots[i + 1] = True           # 다음 칸으로 이동 완료
            A[i + 1] -= 1                  # 이동한 칸의 내구도 1 감소
    robots[N - 1] = False                  # 이동 끝난 후에도 내리는 위치(N-1) 비워주기 (혹시 방금 올라왔다면 내려야 함)

    # 3) 올리는 위치(0)에 로봇 올리기
    if A[0] > 0 and not robots[0]:         # 내구도 남고, 로봇이 없으면
        robots[0] = True                   # 로봇 올림
        A[0] -= 1                          # 올린 칸 내구도 1 감소

    # 4) 종료 조건 체크: 내구도가 0인 칸이 K개 이상이면 종료
    if A.count(0) >= K:
        print(steps)                       # 몇 단계에서 종료되었는지 출력
        break
