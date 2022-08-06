def pp(n, num_list):
    if len(num_list) >= 2*n:
        return num_list
    else:
        p_list = [False, False, True] + [True, False] * (n-1)
        for num, v in enumerate(p_list):
            if num > 2 and v:
                for j in range(2, (2*n)//num +1):
                    p_list[num*j] = False
        num_list = p_list
        return num_list


num_list = [False, False, True] + [True, False] * (123456-1)
for num, v in enumerate(num_list):
    if num > 2 and v:
        for j in range(2, (2*123456)//num +1):
            num_list[num*j] = False

while True:
    n = int(input())
    if n == 0:
        break
    else:
        result = 0
        for num, v in enumerate(pp(n, num_list)):
            if num > n and num <= 2*n and v:
                result = result + 1
        print(result)