'''
1부터 N까지의 자연수를 이진 탐색 트리에 저장하려고 한다.

이진 탐색 트리는 어떤 경우에도 저장된 값이 왼쪽 서브트리의 루트 <현재 노드 <오른쪽 서브 트리의 루트인 규칙을 만족한다.

추가나 삭제가 없는 경우에는, 완전 이진 트리가 되도록 만들면 효율적인 이진 탐색 트리를 만들수 있다.

완전 이진 트리의 노드 번호는 루트를 1번으로 하고 아래로 내려가면서 왼쪽에서 오른쪽 순으로 증가한다.

N이 주어졌을 때 완전 이진 트리로 만든 이진 탐색 트리의 루트에 저장된 값과,
N/2번 노드(N이 홀수인 경우 소수점 버림)에 저장된 값을 출력하는 프로그램을 만드시오.

중위탐색
'''

import sys
sys.stdin = open("swea_5176_이진탐색.txt", "r")

def inorder(k):
    global num
    global n
    if k <= n:
        inorder(k * 2)
        num += 1
        tree[k] = num
        inorder(k * 2 + 1)


test = int(input())

for t in range(1, test + 1):
    n = int(input())

    level = 0
    ck = n
    while ck:
        ck //= 2
        level += 1

    tree = [0 for i in range(2 ** level)]
    num = 0

    inorder(1)

    print(tree)
