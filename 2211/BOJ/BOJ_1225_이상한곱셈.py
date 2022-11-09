A, B = input().split()

if int(A) and int(B):
    cal = {i:0 for i in range(1, 10)}
    result = 0
    for a in A:
        if int(a):
            if cal[int(a)]:
                result += cal[int(a)]
            else:
                tmp = 0
                for b in B:
                    tmp += int(a) * int(b)
                result += tmp
                cal[int(a)] = tmp
    print(result)

else:
    print(0)