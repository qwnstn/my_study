n = int(input())

dark = set()
for i in range(n):
    a, b = map(int, input().split())

    for j in range(a, a+10):
        for k in range(b, b+10):
            dark.add((j, k))

print(len(dark))