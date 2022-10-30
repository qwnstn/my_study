n = int(input()) // 100 * 100
f = int(input())
d = n % f
if d:
    print(str(f - d).zfill(2))
else:
    print('00')