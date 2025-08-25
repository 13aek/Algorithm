import sys
import itertools

N = int(sys.stdin.readline())
sij = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

# 두 시너지의 최소값
min_diff = float("inf")

# 1팀에 들어갈 선수를 뽑는 모든 조합을 생성
for group1 in itertools.combinations(list(range(N)), N // 2):
    # 1팀에 들어가지 않은 선수들로 구성된 조합을 구성
    group2 = tuple(x for x in range(N) if x not in group1)

    # 그룹 1에서 A 음식을 만들때의 시너지
    synergy_1 = 0
    for i, j in itertools.combinations(group1, 2):
        synergy_1 += sij[i][j] + sij[j][i]

    # 그룹 2에서 B 음식을 만들때의 시너지
    synergy_2 = 0
    for i, j in itertools.combinations(group2, 2):
        synergy_2 += sij[i][j] + sij[j][i]

    # 두 음식의 시너지 차이의 최소값 갱신
    min_diff = min(min_diff, abs(synergy_1 - synergy_2))

    # 만약 0이면 반복을 멈춤
    if min_diff == 0:
        break

print(min_diff)