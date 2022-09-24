'''
0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.

가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오.
카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.
'''

import sys
sys.stdin = open("cards.txt", "r")

t = int(input())
for i in range (1, t+1):
    n = int(input())
    a = int(input())

    a_list = [0] * 10
    while a != 0:
        a_list[a % 10] = a_list[a % 10] + 1
        a = a // 10                                   # 카운팅 정렬

    maximum = a_list[0]
    for k in a_list:
        if k > maximum:
            maximum = k                               # 카운팅 된 최대 수

    result_1 = 0                                      # 높은 숫자카드
    result_2 = 0                                      # 숫자카드의 개수
    for num, stack in enumerate(a_list):
        if stack == maximum:
            result_1 = num
            result_2 = stack                          # 9까지 확인하여 최대 값 반영

    print(f'#{i} {result_1} {result_2}')