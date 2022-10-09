import sys
input = sys.stdin.readline

n = int(input())
word = {input().strip() for _ in range(n)}
word = list(word)
word.sort(key=lambda x: (len(x), x))

print('\n'.join(map(str, word)))