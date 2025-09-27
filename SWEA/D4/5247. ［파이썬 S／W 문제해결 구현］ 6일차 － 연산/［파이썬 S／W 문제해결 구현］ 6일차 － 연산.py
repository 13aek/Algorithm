from collections import deque


def bfs(num):
    global result
    q = deque([(num, 0)])
    visited = set()

    while q:
        cur_num, cnt = q.popleft()

        if cur_num in visited:
            continue
        visited.add(cur_num)

        if cur_num == M:
            result = cnt
            return

        for next_num in [cur_num + 1, cur_num - 1, cur_num * 2, cur_num - 10]:
            if 1 <= next_num <= 1000000:
                q.append((next_num, cnt + 1))


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    operation = [1, 1, 2, 10]
    result = 0
    bfs(N)
    print(f"#{tc} {result}")