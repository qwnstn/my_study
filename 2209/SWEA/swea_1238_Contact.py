'''
비상연락망과 연락을 시작하는 당번에 대한 정보가 주어질 때,
가장 나중에 연락을 받게 되는 사람 중 번호가 가장 큰 사람을 구하는 함수를 작성하시오.

'''

import sys
sys.stdin = open("swea_1238_Contact.txt", "r")

def bfs():
    pass

test = 1

for t in range(1, test + 1):
    datalen, start = map(int, input().split())

    data = list(map(int, input().split()))
    contact = dict()
    for i in range(datalen//2):
        a = data[i * 2]
        b = data[i * 2 + 1]
        if contact.get(a):
            contact[a] = contact[a] + [b]
        else:
            contact[a] = [b]
    # print(contact)

    visited = [0 for i in range(len(contact.keys()))]
    # print(visited)

    dfs     스택
    bfs     큐

