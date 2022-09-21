def mid(f, m, e):
    return f + m + e - max(f, m, e) - min(f, m, e)

def length(a1, b1, a2, b2):
    return ((a2 - a1) ** 2 + (b2 - b1) ** 2) ** 0.5


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

ck1_1 = x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3
ck1_2 = x1*y2 + x2*y4 + x4*y1 - x2*y1 - x4*y2 - x1*y4
ck2_1 = x3*y4 + x4*y1 + x1*y3 - x4*y3 - x1*y4 - x3*y1
ck2_2 = x3*y4 + x4*y2 + x2*y3 - x4*y3 - x2*y4 - x3*y2

result = 0
result_list = []

if ck1_1 * ck1_2 * ck2_1 * ck2_2 == 0:
    if ck1_1 == 0:
        if mid(x1, x3, x2) == x3 and mid(y1, y3, y2) == y3:
            result = 1
            if ck1_2 == 0:
                if length(x1, y1, x2, y2) + length(x3, y3, x4, y4) == max(length(x1, y1, x4, y4), length(x2, y2, x4, y4)):
                    result_list.append((x3, y3))
            else:
                result_list.append((x3, y3))

    if ck1_2 == 0:
        if mid(x1, x4, x2) == x4 and mid(y1, y4, y2) == y4:
            result = 1
            if ck1_1 == 0:
                if length(x1, y1, x2, y2) + length(x3, y3, x4, y4) == max(length(x1, y1, x3, y3), length(x2, y2, x3, y3)):
                    result_list.append((x4, y4))
            else:
                result_list.append((x4, y4))

    if ck2_1 == 0:
        if mid(x3, x1, x4) == x1 and mid(y3, y1, y4) == y1:
            result = 1
            if ck2_2 == 0:
                if length(x3, y3, x4, y4) + length(x1, y1, x2, y2) == max(length(x3, y3, x2, y2),
                                                                          length(x4, y4, x2, y2)):
                    result_list.append((x1, y1))
            else:
                result_list.append((x1, y1))

    if ck2_2 == 0:
        if mid(x3, x2, x4) == x2 and mid(y3, y2, y4) == y2:
            result = 1
            if ck2_1 == 0:
                if length(x3, y3, x4, y4) + length(x1, y1, x2, y2) == max(length(x3, y3, x1, y1),
                                                                          length(x4, y4, x1, y1)):
                    result_list.append((x2, y2))
            else:
                result_list.append((x2, y2))

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
            if x1 != x2 and x3 != x4:
                dxdy1 = (y2 - y1) / (x2 - x1)
                dxdy2 = (y4 - y3) / (x4 - x3)
                x = (dxdy1 * x1 - dxdy2 * x3 - y1 + y3) / (dxdy1 - dxdy2)
                y = dxdy1*(x - x1) + y1
                result_list.append((x, y))
            else:
                if x1 == x2:
                    dxdy2 = (y4 - y3) / (x4 - x3)
                    x = x1
                    y = dxdy2*(x - x3) + y3
                    result_list.append((x, y))
                elif x3 == x4:
                    dxdy1 = (y2 - y1) / (x2 - x1)
                    x = x3
                    y = dxdy1 * (x - x1) + y1
                    result_list.append((x, y))

print(result)
if len(result_list):
    print(*result_list[0])