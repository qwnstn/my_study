'''
시간 초과
'''

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

    if word_dict.get(a):
        s = 0
        e = len(word_dict[a]) - 1
        m = (e + s) // 2
        if word_dict[a][e] < l or r < word_dict[a][s]:
            print(0)
            continue
        if e - s > 1:
            while e - s > 1:
                if word_dict[a][e] <= r:
                    r = e
                    break
                elif word_dict[a][m] == r:
                    r = m
                    break
                elif word_dict[a][m] < r:
                    r = m
                    e = m
                    m = (e + s) // 2
                elif r < word_dict[a][m]:
                    r = m - 1
                    s = m
                    m = (e + s) // 2

        else:
            if word_dict[a][e] <= r:
                r = e
            elif word_dict[a][s] <= r < word_dict[a][e]:
                r = s

        s = 0
        e = len(word_dict[a]) - 1
        m = (e + s) // 2
        if e - s > 1:
            while e - s > 1:
                if word_dict[a][s] >= l:
                    l = s
                    break
                elif word_dict[a][m] == l:
                    l = m
                    break
                elif word_dict[a][m] <= l:
                    l = m + 1
                    e = m
                    m = (e + s) // 2
                elif r <= word_dict[a][m]:
                    l = m
                    s = m
                    m = (e + s) // 2

        else:
            if word_dict[a][s] < l <= word_dict[a][e]:
                l = e
            elif l <= word_dict[a][s]:
                l = s
        print(r - l + 1)

    else:
        print(0)