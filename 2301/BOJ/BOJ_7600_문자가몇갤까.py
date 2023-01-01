while True:
    words = input()
    if words == '#':
        break

    result = set()
    for spell in words:
        if ord('A') <= ord(spell) <= ord('Z') or ord('a') <= ord(spell) <= ord('z'):
            result.add(spell.lower())

    print(len(result))
