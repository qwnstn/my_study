num = input()
new = ''

for i in range(1, len(num)+1):           
    new = new + num[-i]             # 거꾸로 쓰기

new_a = int(new[:3])
new_b = int(new[4:])


print(max(new_a, new_b))