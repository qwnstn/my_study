n = int(input())
x, y = map(int, input().split())

if n == 1:
    if x == 1:
        if y == 1:
            print(1, 1)
            print(-1, 1)
        else:
            print(-1, 1)
            print(1, 1)
    else:
        if y == 1:
            print(1, 1)
            print(1, -1)
        else:
            print(1, -1)
            print(1, 1)
else:
    if x == 1:
        if y == 1:
            print(4, 4, 5, 5)
            print(4, 3, 3, 5)
            print(1, 1, 3, 2)
            print(-1, 1, 2, 2)
        elif y == 2:
            print(4, 4, 5, 5)
            print(4, 3, 3, 5)
            print(-1, 1, 3, 2)
            print(1, 1, 2, 2)
        elif y == 3:
            print(1, 1, 5, 5)
            print(-1, 1, 3, 5)
            print(4, 3, 3, 2)
            print(4, 4, 2, 2)
        else:
            print(-1, 1, 5, 5)
            print(1, 1, 3, 5)
            print(4, 3, 3, 2)
            print(4, 4, 2, 2)
    elif x == 2:
        if y == 1:
            print(4, 4, 5, 5)
            print(4, 3, 3, 5)
            print(1, 1, 3, 2)
            print(1, -1, 2, 2)
        elif y == 2:
            print(4, 4, 5, 5)
            print(4, 3, 3, 5)
            print(1, -1, 3, 2)
            print(1, 1, 2, 2)
        elif y == 3:
            print(1, 1, 5, 5)
            print(1, -1, 3, 5)
            print(4, 3, 3, 2)
            print(4, 4, 2, 2)
        else:
            print(1, -1, 5, 5)
            print(1, 1, 3, 5)
            print(4, 3, 3, 2)
            print(4, 4, 2, 2)
    elif x == 3:
        if y == 1:
            print(4, 4, 5, 5)
            print(4, 3, 3, 5)
            print(2, 3, 1, 1)
            print(2, 2, -1, 1)
        elif y == 2:
            print(4, 4, 5, 5)
            print(4, 3, 3, 5)
            print(2, 3, -1, 1)
            print(2, 2, 1, 1)
        elif y == 3:
            print(4, 4, 5, 5)
            print(4, 3, -1, 5)
            print(2, 3, 3, 1)
            print(2, 2, 1, 1)
        else:
            print(4, 4, -1, 5)
            print(4, 3, 5, 5)
            print(2, 3, 3, 1)
            print(2, 2, 1, 1)
    else:
        if y == 1:
            print(4, 4, 5, 5)
            print(4, 3, 3, 5)
            print(2, 3, 1, 1)
            print(2, 2, 1, -1)
        elif y == 2:
            print(4, 4, 5, 5)
            print(4, 3, 3, 5)
            print(2, 3, 1, -1)
            print(2, 2, 1, 1)
        elif y == 3:
            print(4, 4, 5, 5)
            print(4, 3, 5, -1)
            print(2, 3, 3, 1)
            print(2, 2, 1, 1)
        else:
            print(4, 4, 5, -1)
            print(4, 3, 5, 5)
            print(2, 3, 3, 1)
            print(2, 2, 1, 1)