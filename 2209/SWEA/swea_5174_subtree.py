'''
트리의 일부를 서브 트리라고 한다.
주어진 이진 트리에서 노드 N을 루트로 하는 서브 트리에 속한 노드의 개수를 알아내는 프로그램을 만드시오.
'''
import sys
sys.stdin = open("swea_5174_subtree.txt", "r")

test = int(input())

for t in range(1, test + 1):
    e, n = map(int, input().split())

    tree = dict()

    line = list(map(int, input().split()))
    # line = [2, 1, 2, 5, 1, 6, 5, 3, 6, 4]
    # 한 줄 입력을 2개씩(key, value) 사용하기 위해 리스트로 받음

    for i in range(e):
        if tree.get(line[i * 2]):
            tree[line[i * 2]] += [line[i * 2 + 1]]
        else:
            tree[line[i * 2]] = [line[i * 2 + 1]]
    # tree = {2: [1, 5], 1: [6], 5: [3], 6: [4]}
    
    # 트리구조에서 bfs 사용
    stack = [n]
    for i in stack:
        if tree.get(i):             # 트리에 해당 key가 있다면
            stack += tree.get(i)    # value값(list 타입)을 기존 값(list 타입)에 추가

    result = len(stack)             # 답은 stack의 길이
    print(f'#{t} {result}')