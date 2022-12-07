n = input()

word = ''
for i in range(1, int(n)+1):
    word += str(i)

print(word.find(n) + 1)