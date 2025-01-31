N = int(input())
score = list(map(int, input().split()))

new_score= [(s / max(score))* 100 for s in score]

mean = sum(new_score) / N

print(mean)