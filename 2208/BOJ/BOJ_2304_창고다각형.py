'''
12
2 4
11 4
15 8
4 6
5 3
8 10
13 6
7 5
3 6
10 9
9 8
12 9

5
1 1
2 5
3 3
4 5
5 1

10
2 4
11 4
15 1
4 6
5 3
8 10
13 6
9 10
10 5
12 5

101

'''
n = int(input())

all = []
high = 0
for i in range(n):
    l, h = map(int, input().split())
    if high < h:
        high = h
    all.append([l, h])

all.sort(key=lambda x: x[0])            # 데이터 받아서 정렬

ck = []
for k, v in enumerate(all):
    if high == v[1]:
        ck.append(k)                    # ck = [최대값 인덱스 번호들]

lh = 0
for i in range(ck[0]):                # 필요 없는 것들 [0, 0]으로 변경
    if lh < all[i][1]:
        lh = all[i][1]
        continue
    if all[i][1] <= lh:               # 높은 것의 좌측
        all[i] = [0, 0]

rh = 0
for i in range(len(all)-1, ck[-1], -1):   # 높은 것의 우측
    if rh < all[i][1]:
        rh = all[i][1]
        continue
    if all[i][1] <= rh:               # 높은 것의 좌측
        all[i] = [0, 0]

ck2 = []
for k, v in enumerate(all):
    if v != [0, 0]:
        ck2.append(k)                   # ck2 = [값이 있는 것들 인덱스 번호]

result = high
result += high * (all[ck[-1]][0] - all[ck[0]][0])
for i in range(len(ck2)-1):
    if ck2[i] < ck[0]:
        result += all[ck2[i]][1] * (all[ck2[i+1]][0] - all[ck2[i]][0])
    elif ck[-1] <= ck2[i]:
        result += all[ck2[i+1]][1] * (all[ck2[i+1]][0] - all[ck2[i]][0])


print(result)