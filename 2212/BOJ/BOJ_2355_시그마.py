a, b = map(int, input().split())

if a >= 0 and b >= 0:
    print(max(a, b)*(max(a, b) + 1) // 2 - min(a, b)*(min(a, b) - 1) // 2)
elif a < 0 and b < 0:
    a, b = -a, -b
    print(-(max(a, b) * (max(a, b) + 1) // 2 - min(a, b) * (min(a, b) - 1) // 2))
else:
    if a > 0:
        print(a * (a + 1) // 2 - b * (b - 1) // 2)
    else:
        print(b * (b + 1) // 2 - a * (a - 1) // 2)