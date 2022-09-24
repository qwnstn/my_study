'''

N개의 숫자로 이루어진 수열이 주어진다.
맨 앞의 숫자를 맨 뒤로 보내는 작업을 M번 했을 때, 수열의 맨 앞에 있는 숫자를 출력하는 프로그램을 만드시오.
'''

import sys
sys.stdin = open('swea_5097_회전.txt', 'r')

from collections import deque

test = int(input())

for t in range(1, test + 1):
    n, m = map(int, input().split())

    q = deque(map(int, input().split()))

    for i in range(m % n):                      # m을 n으로 나눈 나머지 만큼 반복
        q.append(q.popleft())

    print(f'#{t} {q[0]}')