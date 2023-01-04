words = input().split()
print(words[0][0].upper(), end='')
for word in words[1:]:
    if word not in {'i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili'}:
        print(word[0].upper(), end='')