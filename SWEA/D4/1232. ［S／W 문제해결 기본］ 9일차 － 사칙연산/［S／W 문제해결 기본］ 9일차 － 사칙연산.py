# 후위 순회 함수 정의 ( LRV )
def calc_postorder(node_index):
    # 1. 리프 노드일 때
    if len(tree_info[node_index]) == 2:
        # 노드의 값을 반환
        return int(tree_info[node_index][1])

    # 2. 자식 노드가 왼쪽, 오른쪽  둘 다 있을 때
    else:
        # 왼쪽 오른쪽 인덱스 값
        left_child_idx = int(tree_info[node_index][2])
        right_child_idx = int(tree_info[node_index][3])

        left_val = calc_postorder(left_child_idx)
        right_val = calc_postorder(right_child_idx)

        op = tree_info[node_index][1]
        if op == '+':
            return left_val + right_val
        elif op == '-':
            return left_val - right_val
        elif op == '*':
            return left_val * right_val
        elif op == '/':
            return left_val / right_val


for tc in range(1, 11):
    N = int(input())

    tree_info = [[] for _ in range(N + 1)]
    for _ in range(N):
        node_input = list(input().split())

        tree_info[int(node_input[0])] = node_input

    result = calc_postorder(1)

    print(f"#{tc} {int(result)}")