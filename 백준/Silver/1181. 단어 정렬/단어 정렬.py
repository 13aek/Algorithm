N = int(input())
words = [input().strip() for _ in range(N)]

unique_words = set(words)

sorted_words = sorted(unique_words, key=lambda x: (len(x), x))

for word in sorted_words:
    print(word)