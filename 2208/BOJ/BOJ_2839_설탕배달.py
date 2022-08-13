n = input()         # 문자열

result = 0
if n[-1] == '0' or n[-1] == '5':
    result = int(n) // 5

elif n[-1] == '3' or n[-1] == '6' or n[-1] == '9':
    result = (int(n) - int(n[-1])) // 5
    result = result + int(n[-1]) // 3

elif n[-1] == '2':
    result = (int(n) - int(n[-1]) - 10) // 5
    result = result + (int(n[-1]) + 10) // 3


elif n[-1] == '1' or n[-1] == '4' or n[-1] == '7':
    result = (int(n) - (int(n[-1])//3 +2)*3) // 5 + (int(n[-1])//3 +2)
    if int(n) - 10 < 0:
        result = -1

elif n[-1] == '8':
    result = (int(n) - 3) // 5 + 1

print(result)