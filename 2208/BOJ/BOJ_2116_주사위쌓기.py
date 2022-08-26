'''
5
2 3 1 6 5 4
3 1 2 4 6 5
5 6 4 1 3 2
1 3 6 2 4 5
4 1 6 5 2 3
[(2, 4), (3, 6), (1, 5)]
[(3, 5), (1, 4), (2, 6)]
[(5, 2), (6, 1), (4, 3)]
[(1, 5), (3, 2), (6, 4)]
[(4, 3), (1, 5), (6, 2)]

무조건 6을 넣는 것이 제일 좋음
시작이 정해지면 값도 정해진다.
'''
test = int(input())

result = []
all = []                                        # [ [wntkdnl1], [wnkdnl2]
for t in range(test):
    a, b, c, d, e, f = map(int, input().split())
    all.append([a, f, b, d, c, e])


for i in range(6):
    ck = 0
    cnt = 0
    start = all[ck][i]
    if all[ck].index(start) % 2 == 0:
        pair = all[ck][i + 1]
    else:
        pair = all[ck][i - 1]
    if start != 6 and pair != 6:
        cnt += 6
    else:
        mirror = all[ck][:]
        mirror.remove(start)
        mirror.remove(pair)
        cnt += max(mirror)

    try:
        while True:
            ck += 1
            start = pair
            if all[ck].index(start) % 2 == 0:
                pair = all[ck][all[ck].index(start) + 1]
            else:
                pair = all[ck][all[ck].index(start) - 1]
            if start != 6 and pair != 6:
                cnt += 6
            else:
                mirror = all[ck][:]
                mirror.remove(start)
                mirror.remove(pair)
                cnt += max(mirror)

    except:
        result.append(cnt)

print(max(result))