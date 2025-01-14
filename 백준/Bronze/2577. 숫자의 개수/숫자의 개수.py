A = int(input())
B = int(input())
C = int(input())

dot = str(A * B * C)

count = [0] * 10

for char in dot:
    count[int(char)] += 1

for num in count:
    print(num)