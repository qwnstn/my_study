'''
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 다음과 같이 이루어져 있다.

한 줄에 x1, y1, r1, x2, y2, r2가 주어진다. x1, y1, x2, y2는 -10,000보다 크거나 같고,
10,000보다 작거나 같은 정수이고, r1, r2는 10,000보다 작거나 같은 자연수이다.

각 테스트 케이스마다 류재명이 있을 수 있는 위치의 수를 출력한다.
만약 류재명이 있을 수 있는 위치의 개수가 무한대일 경우에는 -1을 출력한다.

3
0 0 13 40 0 37
0 0 3 0 7 4
1 1 1 1 1 5

2
1
0
'''

t = int(input())

for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)

    else:
        length = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)

        if r1 == length + r2 or r2 == length + r1:
            print(1)
            continue
        elif r1 > length + r2 or r2 > length + r1:
            print(0)
            continue

        ck = r1 + r2
        if length == ck:
            print(1)
        elif length > ck:
            print(0)
        elif length < ck:
            print(2)