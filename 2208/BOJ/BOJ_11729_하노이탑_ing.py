def hanoi(n):
    hanoi(n-1)

    return

n = int(input())
print((2**n)-1)
hanoi(n)