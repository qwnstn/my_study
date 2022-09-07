word = input()
number = [0 for i in range(10)]

for i in word:
    number[int(i)] += 1

for i in range(1, 11):
    print(str(10-i) * number[-i], end='')