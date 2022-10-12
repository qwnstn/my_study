'''
가장 처음에 아기 상어의 크기는 2이고, 아기 상어는 1초에 상하좌우로 인접한 한 칸씩 이동한다.
아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다.

먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기,
그러한 물고기가 여러마리라면,가장 왼쪽에 있는 물고기를 먹는다.

1. 상어와 목표의 거리 계산 - bfs
2. 이동해서 다시 계산
3. 일정 량 이상 잡아먹으면 상어의 크기를 키워서 다시 계산
'''

import sys
input = sys.stdin.readline

n = int(input())
fish = {i: [] for i in range(1, 7)} # {물고기 크기 : [좌표들]}
field = []
for k in range(n):
    a = list(map(int, input().split()))
    field.append(a)
    for i, v in enumerate(a):
        if v != 0 and v != 9:
            fish[v].append([k, i])  # 물고기 좌표
        elif v == 9:
            shark = [k, i]          # 상어 첫 좌표

shark_size = 2   # 상어 크기
eat = 0     # 상어가 먹은 물고기 수
target = []
for i in fish[1]:
