def p_list():
    pp_list = [2]
    pp = [False, False, True] + [True, False] * 499999
    for i in range(3, 1000000, 2):
        if pp[i]:
            pp_list.append(i)
            for p in range(i, 1000001, i):
                pp[p] = False
            pp[i] = True

    return pp_list


pp = p_list()

n = int(input())
for _ in range(n):
    result = 'YES'
    num = int(input())
    num_sqrt = num ** 0.5
    for p in pp:
        if not num % p:
            result = 'NO'
            break

    print(result)