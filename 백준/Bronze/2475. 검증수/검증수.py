numbers = list(map(int,input().split()))

checksum = sum(num**2 for num in numbers) % 10

print(checksum)