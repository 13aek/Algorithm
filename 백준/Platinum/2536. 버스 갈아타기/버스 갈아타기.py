import sys
from collections import deque

line = sys.stdin.readline

m, n = map(int, line().split())
k = int(line())
bus_lines = {}
for _ in range(k):
    bus_num, x1, y1, x2, y2 = map(int, line().split())
    bus_lines[bus_num] = sorted(((x1, y1), (x2, y2)))

sx, sy, dx, dy = map(int, line().split())

transfer_cnt = [float('inf')] * (k + 1)
min_cnt = float('inf')

q = deque()
for bus_num, ((s_x, s_y), (d_x, d_y)) in bus_lines.items():
    if s_x == d_x:
        if s_x == sx and s_y <= sy <= d_y:
            q.append((1, bus_num, s_x, s_y, d_x, d_y))
            transfer_cnt[bus_num] = 1
    else:
        if s_y == sy and s_x <= sx <= d_x:
            q.append((1, bus_num, s_x, s_y, d_x, d_y))
            transfer_cnt[bus_num] = 1

while q:
    bc, bi, cx, cy, ex, ey = q.popleft()

    if bc > min_cnt:
        continue

    if cx == dx and cy <= dy <= ey:
        min_cnt = min(min_cnt, bc)
        continue
    elif cy == dy and cx <= dx <= ex:
        min_cnt = min(min_cnt, bc)
        continue

    # 1. 현재 버스 노선이 수직일 때
    if cx == ex:
        for i in range(1, k + 1):
            (ncx, ncy), (nex, ney) = bus_lines[i]
            # 1.1 다음 버스 노선이 수직이고, 현재 노선이랑 같은 x 좌표라면
            if ncx == nex and ncx == cx:
                # 겹치는 범위가 있다면 (이 부분 조건 설정)
                if max(cy, ncy) <= min(ey, ney):
                    if bc + 1 < transfer_cnt[i]:
                        transfer_cnt[i] = bc + 1
                        q.append((bc + 1, i, ncx, ncy, nex, ney))
            # 1.2 다음 버스 노선이 수평이면
            elif ncy == ney:
                # 현재 x 좌표가 다음 버스 노선이랑 겹친다면 (이 부분 범위 설정)
                if ncx <= cx <= nex and cy <= ncy <= ey:
                    if bc + 1 < transfer_cnt[i]:
                        transfer_cnt[i] = bc + 1
                        q.append((bc + 1, i, ncx, ncy, nex, ney))

    # 2. 현재 버스 노선이 수평일 때
    else:
        for i in range(1, k + 1):
            (ncx, ncy), (nex, ney) = bus_lines[i]
            # 2.1 다음 버스 노선이 수평이고, 현재 노선이랑 같은 y 좌표라면
            if ncy == ney and ncy == cy:
                # (이 부분 조건 설정)
                if max(cx, ncx) <= min(ex, nex):
                    if bc + 1 < transfer_cnt[i]:
                        transfer_cnt[i] = bc + 1
                        q.append((bc + 1, i, ncx, ncy, nex, ney))
            # 2.2 다음 버스 노선이 수직이면
            elif ncx == nex:
                # (이 부분 범위 설정)
                if ncy <= cy <= ney and cx <= ncx <= ex:
                    if bc + 1 < transfer_cnt[i]:
                        transfer_cnt[i] = bc + 1
                        q.append((bc + 1, i, ncx, ncy, nex, ney))

print(min_cnt)
