import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    word, num = map(str, input().split('-'))

    word_num = 0
    for i, v in enumerate(word):
        word_num += (ord(v) - 65) * (26 ** (2-i))

    if abs(word_num - int(num)) <= 100:
        print('nice')
    else:
        print('not nice')