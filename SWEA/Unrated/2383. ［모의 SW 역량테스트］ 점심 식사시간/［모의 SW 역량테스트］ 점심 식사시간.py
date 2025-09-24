from itertools import product


def distance(pr, pc, sr, sc):
    return abs(pr - sr) + abs(pc - sc)


def simulate(stair, people_lst):
    if not people_lst:
        return 0

    sr, sc = stair
    k = room[sr][sc]

    dist = []
    for pr, pc in people_lst:
        dist.append(distance(pr, pc, sr, sc))
    dist.sort()

    q = []
    for arrival in dist:
        if len(q) == 3:
            first_finish = q.pop(0)
            start_time = max(first_finish, arrival)
        else:
            start_time = arrival
        q.append(start_time + k)

    return max(q) + 1


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

    for choice in product([0, 1], repeat=len(people)):
        groupA = [people[i] for i in range(len(people)) if choice[i] == 0]
        groupB = [people[i] for i in range(len(people)) if choice[i] == 1]

        timeA = simulate(stairs[0], groupA)
        timeB = simulate(stairs[1], groupB)

        total_time = max(timeA, timeB)
        min_time = min(min_time, total_time)

    print(f"#{tc} {min_time}")
