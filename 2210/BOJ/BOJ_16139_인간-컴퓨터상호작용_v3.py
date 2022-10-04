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
        if r < word_dict[a][0] or word_dict[a][-1] < l:
            print(0)
            continue

        if l < word_dict[a][0]:
            l = 0
        else:
            try:
                l = word_dict[a].index(l)
            except:
                copy = word_dict[a][:]
                copy.append(l)
                copy.sort()
                l = copy.index(l)

        if r >= word_dict[a][-1]:
            r = len(word_dict[a])
        else:
            try:
                r = word_dict[a].index(r) + 1
            except:
                copy = word_dict[a][:]
                copy.append(r)
                copy.sort()
                r = copy.index(r)

        print(r - l)

    else:
        print(0)