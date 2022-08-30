X = []
Y = []
for i in range(3):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

for i in X:
    if X.count(i) == 1:
        x = i
        break

for i in Y:
    if Y.count(i) == 1:
        y = i
        break

print(x, y)