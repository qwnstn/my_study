na, nb = map(int, input().split())

a = set(map(int, input().split()))
b = set(map(int, input().split()))

c = a-b
print(len(c))
if c:
    c = list(c)
    c.sort()
    print(' '.join(map(str, c)))