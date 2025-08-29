import sys
from itertools import combinations
from collections import deque


# 나눠질 수 있는 그룹인지 판별하는 함수
def is_connected(group, graph):
    """
    group: 검사할 노드 묶음 (반드시 같은 묶음)
    graph: 인접 리스트 (1-indexed)
    return: group이 '하나의 연결'이면 True, 아니면 False
    """
    # 조기 종료 조건
    if not group:   # 빈 그룹은 연결로 볼 수 없음
        return False

    g_set = set(group)
    start = next(iter(g_set))   # 임의의 시작점 하나 선택
    q = deque([start])          # BFS 큐 초기화
    seen = {start}              # 방문한 노드 집합

    while q:
        u = q.popleft()     # 큐에서 하나 꺼내고
        for v in graph[u]:  # u 의 이웃들을 순회
            # 그룹 내부 노드만 타고, 아직 미방문이면 확장
            if v in g_set and v not in seen:
                seen.add(v)
                q.append(v)

    # 방문한 노드 수 == 그룹 전체 노드 수 -> 하나로 연결 
    return len(seen) == len(g_set)



N = int(sys.stdin.readline().strip())
populations = list(map(int, sys.stdin.readline().split()))

graph = [[] for _ in range(N+1)]
for i in range(1, N+1):
    data = list(map(int, sys.stdin.readline().split()))
    graph[i] = data[1:]


ans = float("inf")

nodes = list(range(1, N + 1))

for k in range(1, N//2 + 1):
    for A in combinations(nodes, k):
        a_set = set(A)
        b_set = set(nodes) - a_set

        if not (is_connected(a_set, graph) and is_connected(b_set, graph)):
            continue

        sum_a = sum(populations[a - 1] for a in a_set)
        sum_b = sum(populations[b - 1] for b in b_set)

        diff = abs(sum_a - sum_b)
        if diff < ans:
            ans = diff

if ans == float('inf'):
    ans = -1

print(ans)