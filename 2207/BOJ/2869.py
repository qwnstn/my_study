ABV = list(map(int, input().split()))

A, B, V = ABV
'''
(A-B)*x + A >= V
(A-B)*x >= V-A
x >= (V-A) / (A-B)
'''

if (V-A) % (A-B) == 0:
    result = (V-A) // (A-B) + 1
else:
    result = (V-A) // (A-B) + 2

print(result)