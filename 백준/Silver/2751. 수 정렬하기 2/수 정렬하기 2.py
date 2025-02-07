import sys
N = int(input())
numbers = [int(sys.stdin.readline().strip()) for _ in range(N)]

numbers.sort()

sys.stdout.write('\n'.join(map(str, numbers)) + '\n')
