import sys

line = sys.stdin.readline

# 1. 원래모양
# 2. 왼쪽 90도 회전
# 3. 왼쪽으로 180도 회전
# 4. 왼쪽으로 270도 회전
# 5. 좌우반전
# 6. 왼쪽으로 90도 회전
# 7. 왼쪽으로 180도 회전
# 8. 왼쪽으로 270도 회전
polyomino = {
    # - 모양
    1: [
        [(0, 1), (0, 2), (0, 3)],
        [(1, 0), (2, 0), (3, 0)],
    ],
    # ㅁ 모양
    2: [
        [(0, 1), (1, 0), (1, 1)],
    ],
    # ㄴ 모양
    3: [
        [(1, 0), (2, 0), (2, 1)],
        [(0, 1), (0, 2), (-1, 2)],
        [(0, 1), (1, 1), (2, 1)],
        [(-1, 0), (-1, 1), (-1, 2)],
        [(0, 1), (-1, 1), (-2, 1)],
        [(0, 1), (0, 2), (1, 2)],
        [(0, 1), (1, 0), (2, 0)],
        [(1, 0), (1, 1), (1, 2)],
    ],
    # 번개 모양
    4: [
        [(1, 0), (1, 1), (2, 1)],
        [(0, 1), (-1, 1), (-1, 2)],
        [(-1, 0), (-1, 1), (-2, 1)],
        [(0, 1), (1, 1), (1, 2)],
    ],
    # ㅗ 모양
    5: [
        [(0, 1), (0, 2), (1, 1)],
        [(1, 0), (2, 0), (1, 1)],
        [(0, 1), (0, 2), (-1, 1)],
        [(0, 1), (-1, 1), (1, 1)],
    ]
}


N, M = map(int, line().split())
numbers = [list(map(int, line().split())) for _ in range(N)]

# 추가 코드 (속도를 줄이기 위한?)
m = max([max(l) for l in numbers])

answer = 0
for r in range(N):
    for c in range(M):
        impossible = set()

        for i in range(1, 6):
            for poly in polyomino[i]:
                p_score = numbers[r][c]
                cnt = 1
                for p in poly:
                    nr, nc = r + p[0], c + p[1]

                    if p_score + (4 - cnt) * m <= answer:
                        break
                        
                    if (nr, nc) in impossible:
                        break

                    if 0 > nr or nr >= N or 0 > nc or nc >= M:
                        impossible.add((nr, nc))
                        break

                    p_score += numbers[nr][nc]
                    cnt += 1

                else:
                    if p_score > answer:
                        answer = p_score

print(answer)