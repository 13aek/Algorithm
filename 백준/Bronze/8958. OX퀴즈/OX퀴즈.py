numbers = int(input())

for _ in range(numbers):
    OX = input()
    
    score = 0
    cons = 0
    
    for char in OX:
        if char == 'O':
            cons += 1
            score += cons
        else:
            cons = 0
    print(score)