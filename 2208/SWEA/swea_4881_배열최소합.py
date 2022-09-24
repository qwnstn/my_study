'''
NxN 배열에 숫자가 들어있다. 한 줄에서 하나씩 N개의 숫자를 골라 합이 최소가 되도록 하려고 한다.
단, 세로로 같은 줄에서 두 개 이상의 숫자를 고를 수 없다.

조건에 맞게 숫자를 골랐을 때의 최소 합을 출력하는 프로그램을 만드시오.
'''
import sys

sys.stdin = open('swea_4881_배열최소합.txt', 'r')


test = int(input())

for t in range(1, test +1):
    N = int(input())

    bingo = []
    for i in range(N):
        bingo.append(list(map(int, input().split())))

