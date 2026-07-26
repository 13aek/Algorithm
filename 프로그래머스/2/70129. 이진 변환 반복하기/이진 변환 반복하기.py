def solution(s):
    count = 0
    removed_zero = 0

    while s != "1":
        zero_count = s.count('0')
        removed_zero += zero_count

        one_count = len(s) - zero_count
        s = bin(one_count)[2:]  # 0b 접두사 제거

        count += 1

    return [count, removed_zero]