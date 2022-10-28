'''
1부터 N까지의 수가 있다. 최소공배수가 최대가 되도록 서로 다른 3개의 수를 선택해 보자.

2
3
4

6
12

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
        if b > a:
            a, b = b, a
        while b:
            a, b = b, a % b
        return tmp // a


t = int(input())
for i in range(t):
    n = int(input())

    if n % 2:
        print(U(U(n, n-2), n-1))
    else:
        print(max(U(U(n-1, n-3), n), U(U(n-1, n-3), n-2)))