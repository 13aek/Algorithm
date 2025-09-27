from collections import deque


def bfs(num):
    global result
    q = deque([(num, 0)])
    visited = set([num])

    while q:
        cur_num, cnt = q.popleft()

        if cur_num == M:
            result = cnt
            return

        for next_num in [cur_num + 1, cur_num - 1, cur_num * 2, cur_num - 10]:
            if 1 <= next_num <= 1000000 and next_num not in visited:
                visited.add(next_num)
                q.append((next_num, cnt + 1))


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    result = 0
    bfs(N)
    print(f"#{tc} {result}")