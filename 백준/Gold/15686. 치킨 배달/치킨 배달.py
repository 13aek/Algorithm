import sys
import itertools
from copy import deepcopy


# 거리 구하는 함수
def distance(r1, c1, r2, c2):
    return abs(r1-r2) + abs(c1-c2)


# 치킨 거리를 구하는 함수
def home_chicken_distance(home, chicken):
    home_chicken = [[0] * len(chicken) for _ in range(len(home))]
    for r in range(len(home)):
        for c in range(len(chicken)):
            home_chicken[r][c] = distance(home[r][0], home[r][1], chicken[c][0], chicken[c][1])

    return home_chicken


# 폐업시키고 난 후 치킨 집
def closing_distance(arr, m):
    min_dist = float("inf")
    for comb in itertools.combinations(list(range(len(arr[0]))), m):
        arr_copy = deepcopy(arr)
        for r in range(len(arr_copy)):
            for i in comb:
                arr_copy[r][i] = float("inf")
        dist = min_chicken_distance(arr_copy)
        min_dist = min(min_dist, dist)

    return min_dist


# 치킨집의 좌표를 구하는 함수
def chicken_place(arr):
    chicken_coordinate = []
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 2:
                chicken_coordinate += [[r, c]]

    return chicken_coordinate


# 집의 좌표를 구하는 함수
def home_place(arr):
    home_coordinate = []
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 1:
                home_coordinate += [[r, c]]

    return home_coordinate


# 치킨 거리 합의 최소값을 구하는 함수
def min_chicken_distance(arr):
    min_dist = 0
    for r in range(len(arr)):
        min_dist += min(arr[r])

    return min_dist


# 도시의 가장 작은 치킨거리를 구하는 함수
def calc_distance(arr):
    home = home_place(arr)
    chicken = chicken_place(arr)
    home_chicken = home_chicken_distance(home, chicken)
    min_dist = float('inf')
    min_dist = min(min_dist, closing_distance(home_chicken, len(chicken) - M))

    return min_dist


N, M = map(int, sys.stdin.readline().split())
city_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

result = calc_distance(city_map)
print(result)