result = ['' for _ in range(13)]
result[0] = '-'
for i in range(1, 13):
    result[i] = result[i-1] + ' '*3**(i-1) + result[i-1]
while True:
    try:
        print(result[int(input())])
    except:
        break