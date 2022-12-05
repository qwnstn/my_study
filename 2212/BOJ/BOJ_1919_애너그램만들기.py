a = input()
z = input()

a_d = {chr(i+97): 0 for i in range(26)}
z_d = {chr(i+97): 0 for i in range(26)}

for i in a:
    a_d[i] += 1

for i in z:
    z_d[i] += 1

result = 0
for i in range(26):
    result += abs(a_d[chr(i+97)] - z_d[chr(i+97)])

print(result)