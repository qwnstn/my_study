n = int(input())

equation = ''
for _ in range(2*n - 1):
    tmp = input()
    equation += tmp
    if tmp == '/':
        equation += '/'

print(int(eval(equation)))