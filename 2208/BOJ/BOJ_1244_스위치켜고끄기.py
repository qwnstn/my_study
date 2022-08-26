n = int(input())
switch = list(map(int, input().split()))
stu = int(input())
for i in range(stu):
    s, num = map(int, input().split())

    if s == 1:                                      # 남학생
        for k in range(num-1, len(switch), num):
            switch[k] += 1
    else:                                           # 여학생, 펠린드롬
        switch[num-1] += 1
        k = 1
        try:
            while True:
                if num - 1 - k < 0:
                    break
                if switch[num - 1 + k] % 2 == switch[num - 1 - k] % 2:
                    switch[num - 1 + k] += 1
                    switch[num - 1 - k] += 1
                    k += 1
                else:
                    break
        except:
            pass

for i in range(len(switch)):
    switch[i] %= 2

for i in range(len(switch)):
    print(switch[i], end=' ')
    if (i + 1) % 20 == 0:
        print()
'''
100
1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0
1
1 3
'''