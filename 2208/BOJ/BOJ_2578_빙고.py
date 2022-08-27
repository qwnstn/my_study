bingo = []

for i in range(5):
    bingo.append(list(map(int, input().split())))

bingo2 = [list(i) for i in zip(*bingo)]

X = []
x1 = []
x2 = []
for i in range(5):
    x1.append(bingo[i][i])
    x2.append(bingo[i][4-i])
X.append(x1)
X.append(x2)

lucky = []
for i in range(5):
    a, b, c, d, e = map(int, input().split())
    for j in [a, b, c, d, e]:
        lucky.append(j)



for i in lucky:
    for b in bingo:
        if i in b:
            b.remove(i)
            break
    for b2 in bingo2:
        if i in b2:
            b2.remove(i)
            break
    for x in X:
        if i in x:
            x.remove(i)

    escapex = X.count([])
    escapeb = bingo.count([])
    escapeb2 = bingo2.count([])

    if escapex + escapeb + escapeb2 >= 3:
        result = lucky.index(i) + 1
        break

print(result)