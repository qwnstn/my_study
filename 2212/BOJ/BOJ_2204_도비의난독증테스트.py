while True:
    n = int(input())
    if not n:
        break

    word = []
    for _ in range(n):
        tmp = input()
        word.append((tmp.upper(), tmp))

    word.sort()

    print(word[0][1])