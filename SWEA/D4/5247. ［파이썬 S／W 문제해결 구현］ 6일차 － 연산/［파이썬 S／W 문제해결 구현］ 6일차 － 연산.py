from collections import deque


def bfs(num):
    q = deque([num])
    board[N] = 0

    while q:
        cur_num = q.popleft()

        if cur_num == M:
            break

        for next_num in (cur_num + 1, cur_num - 1, cur_num * 2, cur_num - 10):
            if 1 <= next_num <= 1000000 and board[next_num] == -1:
                q.append(next_num)
                board[next_num] = board[cur_num] + 1


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    board = [-1] * 1000001
    bfs(N)
    print(f"#{tc} {board[M]}")