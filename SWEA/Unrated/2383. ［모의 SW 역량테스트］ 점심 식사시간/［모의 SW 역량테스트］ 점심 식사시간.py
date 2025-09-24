from itertools import permutations


# 계단까지의 거리 구하는 함수
def distance(pr, pc, sr, sc):
    return abs(pr - sr) + abs(pc - sc)


def simulate(stair, people_lst):
    sr, sc = stair
    k = room[sr][sc]
    wait_time = 0

    dist = []
    for pr, pc in people_lst:
        dist.append(distance(pr, pc, sr, sc))
    dist.sort()

    q = []

    while True:
        if len(q) < 3 and dist:
            q.append(dist.pop(0))
        elif len(q) >= 3 and dist:
            if q[0] + k <= dist[0] + wait_time:
                q.pop(0)
                q.append(dist.pop(0) + wait_time)
                wait_time = 0
            else:
                wait_time += 1
        elif not dist:
            time = []
            while q:
                time.append(q.pop(0))
            return max(time) + k + 1


for tc in range(1, int(input()) + 1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]

    people = []
    stairs = []
    for r in range(N):
        for c in range(N):
            if room[r][c] == 1:
                people.append((r, c))
            elif room[r][c] > 1:
                stairs.append((r, c))

    min_time = min(simulate(stairs[0], people), simulate(stairs[1], people))

    for i in range(1, len(people)):
        for perm in permutations(people, i):
            A = perm
            B = list(set(people) - set(perm))

            perm_time = max(simulate(stairs[0], A), simulate(stairs[1], B))

            if perm_time < min_time:
                min_time = perm_time

    print(f"#{tc} {min_time}")