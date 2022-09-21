def mid(f, m, e):
    return f + m + e - max(f, m, e) - min(f, m, e)

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

ck1_1 = x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3
ck1_2 = x1*y2 + x2*y4 + x4*y1 - x2*y1 - x4*y2 - x1*y4
ck2_1 = x3*y4 + x4*y1 + x1*y3 - x4*y3 - x1*y4 - x3*y1
ck2_2 = x3*y4 + x4*y2 + x2*y3 - x4*y3 - x2*y4 - x3*y2

result = 0

if ck1_1 * ck1_2 * ck2_1 * ck2_2 == 0:
    if ck1_1 == 0:
        if mid(x1, x3, x2) == x3 and mid(y1, y3, y2) == y3:
            result = 1
    if ck1_2 == 0:
        if mid(x1, x4, x2) == x4 and mid(y1, y4, y2) == y4:
            result = 1
    if ck2_1 == 0:
        if mid(x3, x1, x4) == x1 and mid(y3, y1, y4) == y1:
            result = 1
    if ck2_2 == 0:
        if mid(x3, x2, x4) == x2 and mid(y3, y2, y4) == y2:
            result = 1

else:
    if ck1_1 * ck1_2 > 0:
        pass
    elif ck2_1 * ck2_2 > 0:
        pass
    elif ck1_1 * ck1_2 < 0:
        if ck2_1 * ck2_2 > 0:
            pass
        elif ck2_1 * ck2_2 < 0:
            result = 1

print(result)