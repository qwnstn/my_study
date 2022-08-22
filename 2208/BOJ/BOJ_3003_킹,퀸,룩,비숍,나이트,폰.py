perfect = [1, 1, 2, 2, 2, 8]

n = list(map(int, input().split()))

need = []
for i in range(6):
    need.append(perfect[i] - n[i])
print(*need)