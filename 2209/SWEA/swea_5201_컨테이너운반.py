'''
화물이 실려 있는 N개의 컨테이너를 M대의 트럭으로 A도시에서 B도시로 운반하려고 한다.

트럭당 한 개의 컨테이너를 운반 할 수 있고, 트럭의 적재용량을 초과하는 컨테이너는 운반할 수 없다.

컨테이너마다 실린 화물의 무게와 트럭마다의 적재용량이 주어지고, A도시에서 B도시로 최대 M대의 트럭이 편도로 한번 만 운행한다고 한다.

이때 이동한 화물의 총 중량이 최대가 되도록 컨테이너를 옮겼다면, 옮겨진 화물의 전체 무게가 얼마인지 출력하는 프로그램을 만드시오.

화물을 싣지 못한 트럭이 있을 수도 있고, 남는 화물이 있을 수도 있다. 컨테이너를 한 개도 옮길 수 없는 경우 0을 출력한다.
'''

import sys;sys.stdin = open('swea_5201_컨테이너운반.txt', 'r')

test = int(input())

for T in range(1, test + 1):
    n, m = map(int, input().split())    
    w = list(map(int, input().split()))     # 화물의 무게
    t = list(map(int, input().split()))     # 트럭이 가능한 무게

    w.sort()
    t.sort()             # 오름차순 정렬

    if w[0] > t[-1]:     # 한 개도 옮기지 못할 경우
        print(f'#{T} 0')
        continue

    result = 0
    for i in range(len(t)):
        while w and t:              # 화물이나 트럭이 없을 때 까지
            if t[-1 - i] < w[-1]:
                w.pop()
            else:
                t.pop()
                result += w.pop()

    print(f'#{T} {result}')