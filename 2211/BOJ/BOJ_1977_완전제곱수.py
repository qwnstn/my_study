# m 이상 n 이하

m = int(input())
n = int(input())

s = int(m**0.5)
if s ** 2 < m:
    s += 1
e = int(n**0.5)

if s > e:
    print(-1)
else:
    total = 0
    for i in range(s, e+1):
        total += i**2
    print(total)
    print(s**2)