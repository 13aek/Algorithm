def solution(s):
    count = 0
    for c in s:
        if c == '(':
            count += 1
        else:
            count -= 1
        if count < 0:  # ')'가 짝을 찾지 못하고 먼저 나온 경우
            return False
    return count == 0  # 마지막에 모두 짝지어졌는지 확인