import sys
from collections import deque

line = sys.stdin.readline

for _ in range(int(line())):
    func_p = list(line().strip())
    n = int(line())
    xn = line().strip()[1:-1]
    if xn:
        xn = deque(map(int, xn.split(',')))
    else:
        xn = deque()

    error = False
    reverse = False

    for c in func_p:
        if c == 'R':
            reverse = not reverse
        elif c == 'D':
            if not xn:
                print('error')
                break
            if reverse:
                xn.pop()
            else:
                xn.popleft()
    else:
        if reverse:
            xn.reverse()
        print('[' + f"{','.join(map(str, xn))}" + ']')