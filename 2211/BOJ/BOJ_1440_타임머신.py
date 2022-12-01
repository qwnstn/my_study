time = input()
# 00:00:00

s = int(time[:2])
m = int(time[3:5])
e = int(time[6:])

if s >= 60 or m >= 60 or e >= 60:
    print(0)
elif 1 <= s <= 12:
    if 1 <= m <= 12:
        if 1 <= e <= 12:
            print(6)
        else:
            print(4)
    else:
        if 1 <= e <= 12:
            print(4)
        else:
            print(2)
else:
    if 1 <= m <= 12:
        if 1 <= e <= 12:
            print(4)
        else:
            print(2)
    else:
        if 1 <= e <= 12:
            print(2)
        else:
            print(0)