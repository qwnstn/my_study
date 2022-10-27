'''
최소공배수의 문제
A, B
ad, bd
abd
AB/d

A, B, C
ad, bd, cd
abcd
ABC/dd

'''
import sys
input = sys.stdin.readline

def U(a, b):
    if not a%b:
        return a
    elif not b%a:
        return b
    else:
        tmp = a*b
        while a*b:
            if a >= b:
                a = a - b
            else:
                a, b = b, a
        return tmp // max(a, b)

n = int(input())
planet = set(map(int, input().split()))

if len(planet) == 1:
    print(list(planet)[0])

else:
    result = 1
    for i in planet:
        result = U(i, result)

    print(result)