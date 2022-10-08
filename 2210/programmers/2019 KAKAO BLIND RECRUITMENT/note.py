import sys
sys.setrecursionlimit(20000)
def pre(idx):
    global dic, PRE
    PRE.append(dic[idx])
    if idx*2 in dic:
        pre(idx*2)
    if idx*2+1 in dic:
        pre(idx*2+1)
def post(idx):
    global dic, POST
    if idx*2 in dic:
        post(idx*2)
    if idx*2+1 in dic:
        post(idx*2+1)
    POST.append(dic[idx])
def solution(nodeinfo):
    global dic,PRE, POST
    PRE=[]
    POST=[]
    answer = [[]]
    dic={}
    L=sorted( range(1,len(nodeinfo)+1),key=lambda x:-nodeinfo[x-1][1])
    dic[1]=L[0]
    for i in range(1,len(L)):
        idx=1
        while idx in dic:
            if nodeinfo[L[i]-1][0]<nodeinfo[dic[idx]-1][0]:
                idx*=2
            else:
                idx=idx*2+1
        dic[idx]=L[i]
    pre(1)
    post(1)
    answer=[PRE,POST]
    return answer