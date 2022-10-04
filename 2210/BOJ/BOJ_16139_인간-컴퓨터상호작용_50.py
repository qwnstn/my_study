import sys
input = sys.stdin.readline

word = list(str(input().strip()))

word_dict = {chr(i):[] for i in range(97, 123)}

for i, v in enumerate(word):
    word_dict[v].append(i)

n = int(input())
for _ in range(n):
    a, l, r = map(str, input().split())
    l = int(l)
    r = int(r)

    result = 0
    for i in word_dict[a]:
        if l <= i <= r:
            result += 1

    print(result)