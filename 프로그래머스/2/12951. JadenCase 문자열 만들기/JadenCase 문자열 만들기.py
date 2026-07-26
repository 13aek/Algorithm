def solution(s):
    answer = ''
    new_word = True

    for c in s:
        if c == ' ':
            answer += c
            new_word = True
        elif c.isalpha():
            answer += c.upper() if new_word else c.lower()
            new_word = False
        else:
            # 숫자 등 알파벳이 아닌 문자
            answer += c
            new_word = False

    return answer