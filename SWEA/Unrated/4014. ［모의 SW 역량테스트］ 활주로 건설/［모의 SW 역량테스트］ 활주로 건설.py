def runway_available(arr):
    global ans
    for r in range(N):
        check_row = arr[r]
        visited = [False] * N
        idx = 0
        for c in range(1, N):
            if not visited[c]:
                if check_row[idx] + 1 == check_row[c]:
                    if idx + 1 < X or True in visited[idx - X + 1: idx + 1]:
                        break
                    else:
                        for i in range(idx - X + 1, idx + 1):
                            visited[i] = True
                        idx = c

                elif check_row[idx] - 1 == check_row[c]:
                    if len(set(check_row[c:c + X])) == 1 and len(check_row[c:c + X]) == X:
                        for i in range(c, c + X):
                            if 0 <= i < N:
                                visited[i] = True
                        idx = c
                    else:
                        break

                elif check_row[idx] == check_row[c]:
                    idx = c

                else:
                    break
        else:
            ans += 1


for tc in range(1, int(input()) + 1):
    N, X = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(N)]
    info_r = list(map(list, zip(*info)))

    ans = 0
    runway_available(info)
    runway_available(info_r)

    print(f"#{tc} {ans}")