from itertools import permutations
from collections import deque


# 계단까지의 거리 구하는 함수
def distance(pr, pc, sr, sc):
    return abs(pr - sr) + abs(pc - sc)


def simulate(stair, people_lst):
    sr, sc = stair
    dist = []
    for pr, pc in people_lst:
        dist.append(distance(pr, pc, sr, sc))
    dist.sort()
    d = deque(dist)
    q = deque()
    wait_time = 0
    k = room[sr][sc]

    while True:
        if len(q) < 3 and d:
            q.append(d.popleft())
        elif len(q) >= 3 and d:
            if q[0] + k <= d[0] + wait_time:
                q.popleft()
                q.append(d.popleft() + wait_time)
                wait_time = 0
            else:
                wait_time += 1
        elif not d:
            time = []
            while q:
                time.append(q.popleft())
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

            perm_time1 = max(simulate(stairs[0], A), simulate(stairs[1], B))
            perm_time2 = max(simulate(stairs[0], B), simulate(stairs[1], A))

            perm_time = min(perm_time1, perm_time2)

            if perm_time < min_time:
                min_time = perm_time

    print(f"#{tc} {min_time}")