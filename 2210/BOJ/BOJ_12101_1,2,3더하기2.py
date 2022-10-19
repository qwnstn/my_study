'''
첫째 줄에 정수 n과 k가 주어진다. n은 양수이며 11보다 작고, k는 2**31-1보다 작거나 같은 자연수이다.
n을 1, 2, 3의 합으로 나타내는 방법 중에서 사전 순으로 k번째에 오는 것을 출력한다.
k번째 오는 식이 없는 경우에는 -1을 출력한다.

1      1    1
2      2    11      2
3      4    111     12      21      3
4      7    1111    112     121     211     13      31  22
5      13   11111
6      24   111111  11112   11121   11211   12111   21111   1113    1131    1311    3111
            1122    1212    1221    2112    2121    2211    123 132 213 231 312 321 33  222
'''

n, k = map(int, input().split())

num_list = [0, 1, 2, 4]
for i in range(4, 12):
    num_list += [num_list[i-1] + num_list[i-2] + num_list[i-3]]
# [0, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504]

result = ''
if k > num_list[n]:
    print(-1)
else:
    while n >= 4:
        if k <= num_list[n-1]:
            result += '1+'
            n -= 1
        elif k <= num_list[n-1] + num_list[n-2]:
            result += '2+'
            k -= num_list[n-1]
            n -= 2
        elif k <= num_list[n-1] + num_list[n-2] + num_list[n-3]:
            result += '3+'
            k -= num_list[n-1] + num_list[n-2]
            n -= 3

    if n == 3:
        if k == 1:
            result += '1+1+1'
        elif k == 2:
            result += '1+2'
        elif k == 3:
            result += '2+1'
        elif k == 4:
            result += '3'
    elif n == 2:
        if k == 1:
            result += '1+1'
        elif k == 2:
            result += '2'
    elif n == 1:
        result += '1'

print(result)
'''
50 9999999999999
'''