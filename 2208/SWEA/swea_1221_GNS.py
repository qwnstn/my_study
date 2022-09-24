'''
숫자 체계가 우리와 다른 어느 행성이 있다. 아래는 이 행성에서 사용하는 0 ~ 9의 값을 순서대로 나타낸 것이다.

"ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"

0 ~ 9 의 값을 나타내는 단어가 섞여 있는 문자열을 받아 작은 수부터 차례로 정렬하여 출력하는 프로그램을 작성하라.

예를 들어 입력 문자열이 "TWO NIN TWO TWO FIV FOR" 일 경우 정렬한 문자열은 "TWO TWO TWO FOR FIV NIN" 이 된다.

'''

import sys
sys.stdin = open("swea_1221_GNS.txt", "r")

test = int(input())

num_dict = {"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}

for t in range(1, test+1):
    testcase, n = map(int, input().lstrip('#').split())
    num_list = list(map(str, input().split()))

    num_list.sort(key=lambda x: num_dict[x])        # dict와 list연결 / x = num_list

    print(f'#{t}')
    print(*num_list)