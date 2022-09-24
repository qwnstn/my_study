'''
사칙연산 “+, -, *, /”와 양의 정수로만 구성된 임의의 이진 트리가 주어질 때,
이를 계산한 결과를 출력하는 프로그램을 작성하라.

계산 중간 과정에서의 연산은 모두 실수 연산으로 한다.
결과값은 소수점 아래는 버리고 정수로 출력한다.

후위표기법
'''

import sys
sys.stdin = open("swea_1232_사칙연산.txt", "r")

def tree_cal(k = '1'):
    if tree[k][1]:  # 자식이 있을 때  = 연산기호
        a = tree_cal(tree[k][1][0])     # 왼쪽 자식
        b = tree_cal(tree[k][1][1])     # 오른쪽 자식

        if tree[k][0] == '+':
            return a + b
        elif tree[k][0] == '-':
            return a - b
        elif tree[k][0] == '*':
            return a * b
        elif tree[k][0] == '/':
            return a / b

    else:                       # 자식이 없을 때 = 숫자
        return float(tree[k][0])

test = 10

for t in range(1, test + 1):
    n = int(input())

    tree = dict()
    # {'1': ['-', ['2', '3']], '2': ['-', ['4', '5']], '3': ['10', []], '4': ['88', []], '5': ['65', []]}

    for i in range(n):
        a, b, *c = map(str, input().split())
        tree[a] = [b, c]

    print(f'#{t} {int(tree_cal())}')