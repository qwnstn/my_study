'''
주어진 N 길이의 숫자열을 오름차순으로 정렬하여 출력하라.
'''

import sys
sys.stdin = open("swea_1966_숫자를정렬하자_선택정렬.txt", "r")

test = int(input())

for t in range(1, test+1):
    n = int(input())

    for i in range(n):
        num = list(map(int, input().split()))
