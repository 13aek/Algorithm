import sys

def dfs(cur_num, cur_idx, path):
    global max_len
    global path_origin

    if cur_num < 0:
        if len(path) > max_len:
            max_len = len(path)
            path_origin = path[:]
        return

    path.append(cur_num)
    next_num = path[cur_idx - 1] - path[cur_idx]
    dfs(next_num, cur_idx + 1, path)
    path.pop()


line = sys.stdin.readline().strip()

N = int(line)

max_len = 0
path_origin = []

for i in range(N, -1, -1):
    dfs(i, 1, [N])

print(max_len)
print(*path_origin)