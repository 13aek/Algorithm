from itertools import combinations

N, M = map(int, input().split())

numbers = list(map(int,input().split()))

max_sum = 0
for combo in combinations(numbers, 3):
    current_sum = sum(combo)
    if current_sum <= M:
        max_sum = max(max_sum, current_sum)
        
print(max_sum)