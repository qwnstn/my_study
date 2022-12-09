while True:
    n, a, w = map(str, input().split())
    if n == '#':
        break
    if int(a) > 17:
        print(n, 'Senior')
        continue
    if int(w) >= 80:
        print(n, 'Senior')
        continue
    print(n, 'Junior')