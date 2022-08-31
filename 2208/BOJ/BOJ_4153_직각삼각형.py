import sys

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == b == c == 0:
        break

    a2 = a**2
    b2 = b**2
    c2 = c**2

    if max(a2, b2, c2) * 2 == a2 + b2 + c2:
        print('right')
    else:
        print('wrong')