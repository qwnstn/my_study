'''
식재료들을 각각 N / 2개씩 나누어 두 개의 요리를 하려고 한다. (N은 짝수이다.)

가지고 있는 식재료를 이용해 A음식과 B음식을 만들 때,
두 음식 간의 맛의 차이가 최소가 되는 경우를 찾고 그 최솟값을 정답으로 출력하는 프로그램을 작성하라.

'''

import sys
sys.stdin = open("swea_4012_요리사.txt", "r")

def com(x, y=0):                                # x = 주어진 리스트의 길이
    if len(food) - y < x//2 - len(combi):       # 가지치기
        return

    if len(combi) == x//2:
        all.append(combi[:])
    else:
        for k in range(y, len(food)):
            combi.append(food[k])
            com(n, k+1)
            combi.pop()


test = int(input())

for t in range(1, test + 1):
    n = int(input())

    S = []
    for i in range(n):
        S.append(list(map(int, input().split())))

    food = [i for i in range(n)]

    all = []
    combi = []
    com(n)

    result = 0
    for i in S:
        result += sum(i)

    for a in all:
        A = 0
        B = 0
        not_all = [i for i in range(n)]
        for i in a:
            not_all.remove(i)       # a의 여집합

        for i in a:
            for j in a:
                A += S[i][j]

        for i in not_all:
            for j in not_all:
                B += S[i][j]

        ck = abs(A - B)

        if ck <= result:
            result = ck

    print(f'#{t} {result}')
