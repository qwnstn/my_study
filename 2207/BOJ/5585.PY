n = int(input())

change = 1000 - n
change_list = [500, 100, 50, 10, 5, 1]
result = 0

for i in change_list:
    result = result + change // i
    change = change - (change // i) * i

print(result)