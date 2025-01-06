N = int(input())

numbers = input().strip()

result = sum(int(num) for num in numbers)

print(result)