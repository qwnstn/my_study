'''

다음 주어진 조건에 따라 n개의 수를 처리하면 8자리의 암호를 생성할 수 있다.

- 8개의 숫자를 입력 받는다.

- 첫 번째 숫자를 1 감소한 뒤, 맨 뒤로 보낸다.

다음 첫 번째 수는 2 감소한 뒤 맨 뒤로, 그 다음 첫 번째 수는 3을 감소하고 맨 뒤로, 그 다음 수는 4, 그 다음 수는 5를 감소한다.

이와 같은 작업을 한 사이클이라 한다.

- 숫자가 감소할 때 0보다 작아지는 경우 0으로 유지되며, 프로그램은 종료된다. 이 때의 8자리의 숫자 값이 암호가 된다.

'''

import sys
sys.stdin = open('swea_1225_암호생성기.txt', 'r')

from collections import deque

for t in range(1, 11):
    n = int(input())
    pw = deque(map(int, input().split()))               # deque([9550, 9556, 9550, 9553, 9558, 9551, 9551, 9551])

    while pw[-1] != 0:                                  # 마지막이 0이 아닐때 까지
        for i in range(1, 6):                           # 한 세트에 5번
            pw.append(pw.popleft() - i)                 # 왼쪽 값 빼서 계산 후 우측으로 넣기
            if pw[-1] <= 0:                             # 세트 중 0 이하로 떨어지면 0을 주고 세트 종료 & while문 종료
                pw[-1] = 0
                break

    print(f'#{t} ', end='')
    print(*pw)