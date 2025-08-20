from collections import deque


# 가위바위보 승자 정하는 함수
def rock_scissor_paper(a, b, i, j):
    """
    가위바위보 승자 누군지 반환하는 함수
    :param a: 가위, 바위, 보 중 하나
    :param b: 가위, 바위, 보 중 하나
    :param i: a의 인덱스
    :param j: b의 인덱스
    :return: 이긴사람
    """
    if a - b == -1 or a - b == 2:
        return j
    elif a == b:
        if i < j:
            return i
        else:
            return j
    else:
        return i


# 두 그룹으로 나누는 함수
def divide_group(q):
    divide = (1 + len(q)) // 2
    q1 = deque()
    q2 = deque()
    for i in range(divide):
        q1.append(q[i])
    for j in range(divide, len(q)):
        q2.append(q[j])
    return q1, q2


# 그룹의 승자를 반환하는 함수
def winner_q(q):
    if len(q) > 2:
        q1, q2 = divide_group(q)
        winner_1 = winner_q(q1)
        winner_2 = winner_q(q2)
        return winner_q(winner_1 + winner_2)
    elif len(q) == 1:
        return q

    else:
        a = q.popleft()
        b = q.popleft()
        winner = rock_scissor_paper(a[1], b[1], a[0], b[0])
        if winner == a[0]:
            q.append(a)
        else:
            q.append(b)

    return q


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    lst_idx = [[idx + 1, i] for idx, i in enumerate(lst)]
    winners = winner_q(lst_idx)
    print(f"#{tc} {winners[0][0]}")