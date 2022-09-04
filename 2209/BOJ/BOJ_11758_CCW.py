'''
신발끈 공식

'''

p = [0 for i in range(4)]

for i in range(1, 4):
    p[i] = list(map(int, input().split()))

p[3][0] -= p[1][0]
p[3][1] -= p[1][1]
p[2][0] -= p[1][0]
p[2][1] -= p[1][1]


if p[2][0] == 0 and p[3][0] == 0:
    print(0)

elif p[2][0] == 0:
    if p[3][0] > 0:
        print(-1)
    else:
        print(1)

elif p[3][0] == 0:
    if p[3][1] > 0:
        if p[2][0] > 0:
            print(1)
        else:
            print(-1)
    else:
        if p[2][0] > 0:
            print(-1)
        else:
            print(1)

else:
    p2 = p[2][1] / p[2][0]
    p3 = p[3][1] / p[3][0]

    if p2 == p3 or p2 == -p3:
        print(0)
    elif p2 > 0:
        if p[2][0] > 0:
            if p[3][0] > 0:
                if p3 > p2:
                    print(1)
                else:
                    print(-1)
            else:
                if p[3][0] < 0:
                    if p3 > p2:
                        print(-1)
                    else:
                        print(1)
        else:
            if p[3][0] > 0:
                if p3 > p2:
                    print(-1)
                else:
                    print(1)
            else:
                if p[3][0] < 0:
                    if p3 > p2:
                        print(1)
                    else:
                        print(-1)
    elif p2 < 0:
        if p[2][0] > 0:
            if p[3][0] > 0:
                if p3 > p2:
                    print(1)
                else:
                    print(-1)
            else:
                if p3 > p2:
                    print(-1)
                else:
                    print(1)
        else:
            if p[3][0] > 0:
                if p3 > p2:
                    print(-1)
                else:
                    print(1)
            else:
                if p3 > p2:
                    print(1)
                else:
                    print(-1)