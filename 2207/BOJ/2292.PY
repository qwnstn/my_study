'''
1           0
2~7         6
8~19        12
20~37       18  
38~61       24
62~91       30
'''

N = int(input())
sum = 1
ck = 1
while sum < N:
    sum = sum + ck*6
    ck = ck+1

print(ck)