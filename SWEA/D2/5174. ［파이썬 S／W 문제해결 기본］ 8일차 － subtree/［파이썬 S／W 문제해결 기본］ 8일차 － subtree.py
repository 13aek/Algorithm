# 전위 순회 함수 정의
def preorder(node):
    nodes = []
    if node != 0:
        nodes.append(node)
        nodes += preorder(left[node])
        nodes += preorder(right[node])

    return nodes



T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split())

    edge = list(map(int, input().split()))

    left = [0] * (E + 2)
    right = [0] * (E + 2)

    for i in range(E):
        parent, child = edge[i * 2], edge[i * 2 + 1]

        if left[parent] == 0:
            left[parent] = child
        else:
            right[parent] = child

    sub_tree_len = len(preorder(N))
    print(f"#{tc} {sub_tree_len}")
