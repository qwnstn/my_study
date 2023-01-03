while True:
    words = input()
    if words == '#':
        break

    result = set()
    for spell in words:
        if ord('A') <= ord(spell) <= ord('Z') or ord('a') <= ord(spell) <= ord('z'):
            result.add(spell.lower())

<<<<<<< HEAD
    print(len(result))
=======
    print(len(result))
>>>>>>> c6ef133ada8ddc82c4affb03ac35853b17cd0432
