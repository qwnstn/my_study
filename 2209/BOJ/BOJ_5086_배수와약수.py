import sys

x = y = 1
while not (x == 0 and y == 0):
    x, y = map(int, sys.stdin.readline().split())
    if x == 0 and y == 0:
        continue
    if y == 0:
        print('neither')
    elif x == 0:
        print('multiple')
    elif x % y == 0:
        print('multiple')   # 배수
    elif y % x == 0:
        print('factor')     # 약수
    else:
        print('neither')