'''
두 개의 문자열 str1과 str2가 주어진다.

문자열 str1에 포함된 글자들이 str2에 몇 개씩 들어있는지 찾고,
그중 가장 많은 글자의 개수를 출력하는 프로그램을 만드시오.

예를 들어 str1 = “ABCA”, str2 = “ABABCA”인 경우,
str1의 A가 str2에 3개 있으므로 가장 많은 글자가 되고 3을 출력한다.

파이썬의 경우 딕셔너리를 이용할 수 있다.
'''

import sys

sys.stdin = open("swea_4865_글자수.txt", "r")

test = int(input())

for t in range(1, test+1):
    n = list(set(input()))          # 중복제거, set만 쓰면 인덱스를 불러올 수 없음
    m = input()

    ck = -1
    result = 0
    while True:
        ck = ck + 1

        if m.count(n[ck]) > result:
            result = m.count(n[ck])

        if n[ck] == n[-1]:          # 중단용
            break

    print(f'#{t} {result}')