'''
“N개의 피자 조각을 K명의 학생들에게 나눠주되,
모든 학생들은 한 조각 이상 받아야 하며, 인접한 조각들을 같은 학생에게 주면 안된다.
이러한 조건을 만족하며 피자 조각을 나눠주는 경우의 수를 구하여라”

피자 분배 경우의 수를 1,000,000,007로 나눈 나머지를 출력하라.
'''

import sys;sys.stdin=open('swea_8660_Pizza.txt', 'r')

test = int(input())

for t in range(1, test +1):
    n, k = map(int, input().split())

