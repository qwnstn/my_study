# 시간 초과

def func(k, n):
    ck = 0
    if k != 0:
        for i in range(1, n+1):
            ck = ck + func(k-1, i)
        return ck
    else:
        return n
    
t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())

    print(func(k,n))