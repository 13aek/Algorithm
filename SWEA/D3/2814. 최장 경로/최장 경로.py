def dfs(node, visited, length):
    global result
    result = max(result, length)

    for next_node in adj_list[node]:
        if not visited[next_node]:
            visited[next_node] = True
            dfs(next_node, visited, length + 1)
            visited[next_node] = False


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())

    adj_list = [[] for _ in range(N + 1)]
    for i in range(M):
        a, b = map(int, input().split())
        adj_list[a].append(b)
        adj_list[b].append(a)

    result = 1
    for i in range(1, N + 1):
        visited = [False] * (N + 1)
        visited[i] = True
        dfs(i, visited, 1)

    print(f"#{tc} {result}")