'''
101, 201, ... H01   H
102, 202, ... H02   H
...                 ...
10W, 20W, ... H0W   H
'''

t = int(input())

for i in range(t):
    h, w, n = list(map(int, input().split()))

    # 나머지를 0부터 시작하는 것이 표시하기가 좋음으로 n-1로 비교

    if (n-1)//h + 1 <10 :
        result = f'{(n-1)%h + 1}0{(n-1)//h + 1}'
    else:
        result = f'{(n-1)%h + 1}{(n-1)//h + 1}'
    
    print(result)