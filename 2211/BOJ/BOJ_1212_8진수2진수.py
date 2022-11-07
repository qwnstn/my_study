n = input()

result = ''
for i in n:
    result += str(bin(int(i)))[2:].zfill(3)
print(int(result))