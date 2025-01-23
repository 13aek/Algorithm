def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

N = int(input())
numbers = list(map(int, input().split()))

count = sum(1 for number in numbers if is_prime(number))

print(count)