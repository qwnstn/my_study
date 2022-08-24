'''
5
ABC*+DE/-
1
2
3
4
5
'''
N = int(input())

arr = list(input())

for i in range(len(arr)):
    if 65 <= ord(arr[i]) <= 90:
        a = input()
        b = arr[i]
        for x in range(len(arr)):
            if arr[x] == b:
                arr[x] = a


sta = []

for i in arr:
    if i.isdecimal():
        sta.append(i)
    else:
        if i == '*' and len(sta) >= 2:
            a = sta.pop()
            b = sta.pop()
            sta.append(float(a) * float(b))
        elif i == '+' and len(sta) >= 2:
            c = sta.pop()
            d = sta.pop()
            sta.append(float(c) + float(d))
        elif i == '-' and len(sta) >= 2:
            e = sta.pop()
            f = sta.pop()
            sta.append(float(f) - float(e))
        elif i == '/' and len(sta) >= 2:
            g = sta.pop()
            h = sta.pop()
            sta.append(float(h) / float(g))
print(f"{float(sta[0]):.2f}")
