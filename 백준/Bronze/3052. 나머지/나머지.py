numbers = [int(input()) for _ in range(10)]

remainders = [num % 42 for num in numbers]

unique = len(set(remainders))

print(unique)