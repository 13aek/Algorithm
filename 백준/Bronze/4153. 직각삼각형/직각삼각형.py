while True:
    sides = list(map(int, input().split()))
    if sides == [0, 0, 0]:
        break
    
    sides.sort()
    a,b,c = sides
    
    if a**2 + b**2 == c**2:
        print("right")
    else:
        print("wrong")