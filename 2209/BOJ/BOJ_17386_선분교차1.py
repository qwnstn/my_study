x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

ck1_1 = x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3
ck1_2 = x1*y2 + x2*y4 + x4*y1 - x2*y1 - x4*y2 - x1*y4
ck2_1 = x3*y4 + x4*y1 + x1*y3 - x4*y3 - x1*y4 - x3*y1
ck2_2 = x3*y4 + x4*y2 + x2*y3 - x4*y3 - x2*y4 - x3*y2

if ck1_1 * ck1_2 > 0:
    print(0)
elif ck2_1 * ck2_2 > 0:
    print(0)
elif ck1_1 * ck1_2 < 0:
    if ck2_1 * ck2_2 > 0:
        print(0)
    elif ck2_1 * ck2_2 < 0:
        print(1)