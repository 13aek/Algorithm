# DFS 탐색 함수 정의
def dfs(current_student, adj_lst):
    global visited

    visited[current_student] = True

    if not adj_lst[current_student]:
        return

    for next_student in adj_lst[current_student]:
        if not visited[next_student]:
            dfs(next_student, adj_lst)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = int(input())
    compare_h = [list(map(int, input().split())) for _ in range(M)]

    adj_list_t = [[] for _ in range(N+1)]
    for com in compare_h:
        adj_list_t[com[0]] += [com[1]]

    adj_list_s = [[] for _ in range(N + 1)]
    for com in compare_h:
        adj_list_s[com[1]] += [com[0]]

    cnt = 0
    for i in range(1, N+1):
        visited = [False] * (N + 1)
        dfs(i, adj_list_t)
        dfs(i, adj_list_s)

        if False not in visited[1:]:
            cnt += 1

    print(f"#{tc} {cnt}")