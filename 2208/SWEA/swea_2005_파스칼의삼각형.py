'''
크기가 N인 파스칼의 삼각형을 만들어야 한다.

파스칼의 삼각형이란 아래와 같은 규칙을 따른다.

1. 첫 번째 줄은 항상 숫자 1이다.

2. 두 번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합으로 구성된다.

N이 4일 경우,
1
1 1
1 2 1
1 3 3 1
'''

import sys

sys.stdin = open("swea_2005_파스칼의삼각형.txt", "r")

test = int(input())

# for t in range(1, test+1):
#     n = int(input())
#
#     print(f'#{t}')
#     for i in range(n):
#         x = str(11**i)
#         print(' '.join(x))
#     자릿수가 바뀌면 먹지 않음(n >= 6)

    # 리스트화 해서 더하기

for t in range(1, test+1):
    pascal = [1]  # pascal 초기값
    N = int(input())  # 구할 개수
    print(f'#{t}', pascal[0], sep='\n')  # 첫 항 출력

    while len(pascal) < N:  # 개수를 충족할 때까지 반복문 진행
        for i in range(len(pascal) - 1, 0, -1):
            pascal[i] = pascal[i] + pascal[i - 1]  # 내부값 파스칼 조건에 따른 변경 진행
        pascal.append(1)
        print(' '.join(map(str, pascal)))