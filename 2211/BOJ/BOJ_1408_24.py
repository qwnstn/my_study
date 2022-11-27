s = input().split(':')
e = input().split(':')

s_sec = 3600 * int(s[0]) + 60 * int(s[1]) + int(s[2])
e_sec = 3600 * int(e[0]) + 60 * int(e[1]) + int(e[2])

if e_sec > s_sec:
    result_sec = e_sec - s_sec
else:
    result_sec = e_sec - s_sec + 3600 * 24

result = [0, 0, 0]
for i in range(3):
    result[i] = result_sec // 60**(2-i)
    result_sec -= 60**(2-i) * result[i]
    result[i] = str(result[i]).zfill(2)

print(':'.join(result))

