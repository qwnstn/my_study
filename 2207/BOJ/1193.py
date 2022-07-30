'''
순번    개수     분모분자합
(X)     (ck)    (result)
1       1       2   
2~3     2       3
4~6     3       4
7~10    4       5
11~15   5       6
16~21   6       7
'''
X = int(input())

sum = 1
ck = 1

while sum < X:
    ck = ck + 1
    sum = sum + ck

result = ck + 1
a = X - (sum - ck)  # result를 나눠가질 숫자

if ck % 2 == 0:
    print(f'{a}/{result - a}')
else:
    print(f'{result - a}/{a}')