'''
유클리드 호제법
'''
import sys

input = sys.stdin.readline

n = int(input())
for i in range(n):
    a, b = map(int, input().split())

    result = a * b

    while a * b != 0:
        if a >= b:
            a = a % b
        else:
            a, b = b, a

    if result * a:
        print(result // a)
    else:
        print(result // b) 