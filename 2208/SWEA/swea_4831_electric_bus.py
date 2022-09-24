#  솔루션 코드를 작성합니다.

'''
A도시는 전기버스를 운행하려고 한다.
전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서, 중간에 충전기가 설치된 정류장을 만들기로 했다.

버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.

충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.

만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다.
출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.
'''

import sys
sys.stdin = open("electric_bus.txt", "r")


t = int(input())
for i in range(1, t+1):
    k, n, m = map(int, input().split())
    stop = list(map(int, input().split())) + [n]  #1-1 골인지점도 충전소로 생각한다.

    bus = 0
    result = 0
    while bus != n:
        for a in range(k, 0, -1):               # k ~ 1
            if bus + a in stop:
               bus = bus + a
               result = result + 1
               break
            else:
               if a == 1:
                   bus = n                  # while문 탈출용
                   result = 1               #1-3 결과적으로 1을 빼주기 때문에 result를 1로 준다

    print(f'#{i} {result - 1}')             #1-2 n도 result에 포함되므로 1을 빼준다