def lucky7(n):
    global over

    if len(mini) == n:
        return

    for m in mini_all:
        if m not in mini:
            mini.append(m)
            over -= m
            lucky7(n)
            if over == 0 and len(mini) == n:
                return
            mini.pop()
            over += m

mini_all = []
for i in range(9):
    mini_all.append(int(input()))

over = sum(mini_all) - 100

mini = []
lucky7(2)

for i in mini:
    mini_all.remove(i)

mini_all.sort()
for i in mini_all:
    print(i)