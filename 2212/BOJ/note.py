num = int(input())
if num >= 0:
    print(len(bin(num)[2:]))
else:
    print(32)