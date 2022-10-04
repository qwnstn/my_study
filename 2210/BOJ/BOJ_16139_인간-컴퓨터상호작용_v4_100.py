import sys
input = sys.stdin.readline

word = list(str(input().strip()))

word_list = [0 for i in range(26)]

all_word = [word_list[:]]

for i, v in enumerate(word):
    word_list[ord(v) - 97] += 1
    all_word.append(word_list[:])

result = []
n = int(input())
for _ in range(n):
    a, l, r = map(str, input().split())
    l = int(l)
    r = int(r) + 1

    result.append(all_word[r][ord(a) - 97] - all_word[l][ord(a) - 97])

print('\n'.join(map(str, result)))