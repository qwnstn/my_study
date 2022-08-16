'''
n을 딕셔너리 자료형으로 만들어 호출

정렬하여 리스트 뒤에서부터 pop하고
마지막 부분에선 try except를 하여 따로 조건 제시 
'''

import sys

n = int(sys.stdin.readline().rstrip())
nlist = list(map(int, sys.stdin.readline().split()))
nlist.sort()

ndict = dict()
while nlist != []:
    ck = 1
    try:
        while nlist[-1] == nlist[-2]:
            ck = ck + 1
            nlist.pop()
        ndict[nlist.pop()] = ck
    except:
        if ndict.get(nlist[-1]) == None:
            ndict[nlist.pop()] = ck
        else:
            ndict[nlist[-1]] = ndict[nlist[-1]] +1


m = int(sys.stdin.readline().rstrip())
mlist = list(map(int, sys.stdin.readline().split()))

result = []
for i in mlist:
    if ndict.get(i) == None:
        result.append(0)
    else:
        result.append(ndict.get(i))

print(' '.join(map(str, result)))