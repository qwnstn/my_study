'''


'''

import sys;sys.stdin = open('swea_1873_상호의배틀필드.txt', 'r')

test = int(input())

for t in range(1, test + 1):
    h, w = map(int, input().split())

    field = []
    for _ in range(h):
        field.append([input()])

    n = int(input())
