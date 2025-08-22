# 중위 순회 함수 정의 ( LVR )
def calc_inorder(node_index):
    # 합친 문자열을 담을 빈 문자열 정의
    words = ''

    # 1. 리프 노드일 때
    if len(tree_info[node_index]) == 2:
        # 노드의 값을 반환
        return tree_info[node_index][1]

    # 2. 자식 노드가 한 개 뿐일 때
    elif len(tree_info[node_index]) == 3:
        # 왼쪽 자식의 인덱스 값
        left_child_idx = int(tree_info[node_index][2])

        # 2_1 왼쪽 자식 부터
        words += calc_inorder(left_child_idx)
        # 2_2 자기 자신
        words += tree_info[node_index][1]

    # 3. 자식 노드가 왼쪽, 오른쪽  둘 다 있을 때
    else:
        # 왼쪽 오른쪽 인덱스 값
        left_child_idx = int(tree_info[node_index][2])
        right_child_idx = int(tree_info[node_index][3])

        # 3_1 왼쪽 자식 부터
        words += calc_inorder(left_child_idx)
        # 3_2 자기 자신
        words += tree_info[node_index][1]
        # 3_3 오른쪽 자식
        words += calc_inorder(right_child_idx)

    return words


for tc in range(1, 11):
    N = int(input())    # 정점 V의 총 수

    # 입력받은 트리의 정보를 저장할 빈 리스트
    tree_info = [[] for _ in range(N + 1)]
    # 정점의 총 수 만큼 반복
    for _ in range(N):
        # 노드의 정보를 그대로 입력 받음
        node_input = input().split()
        # 입력받은 정점의 번호를 인덱스로 노드의 정보를 저장
        tree_info[int(node_input[0])] = node_input

    # 1을 루트로 시작하는 중위 순회 계산 함수 호출
    total_word = calc_inorder(1)

    print(f"#{tc} {total_word}")