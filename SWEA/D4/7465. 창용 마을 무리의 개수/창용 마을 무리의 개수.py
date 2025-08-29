def dfs(current_node, adj_list, visited):
    visited[current_node] = True

    for next_node in adj_list[current_node]:
        if not visited[next_node]:
            dfs(next_node, adj_list, visited)


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    relations = [[] for _ in range(N + 1)]

    for _ in range(1, M+1):
        a, b = map(int, input().split())
        relations[a].append(b)
        relations[b].append(a)

    visited = [False] * (N + 1)
    ans = 0
    for i in range(1, N+1):
        if not visited[i]:
            ans += 1
            dfs(i, relations, visited)

    print(f"#{tc} {ans}")