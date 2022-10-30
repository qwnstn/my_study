'''
1 - jhnah917
2 - jhnan917
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
for i in range(n):
    input()

color = {'R':0, 'B':0, 'G':0}
for i in range(m):
    a, b, c = map(str, input().split())
    color[c] += 1

'''
1 - jhnah917 = color['R'] + color['G']
2 - jhnan917 = color['B'] + color['G']
'''

if color['G'] % 2:
    jhnah917 = color['R'] + 1
    jhnan917 = color['B']

else:
    jhnah917 = color['R']
    jhnan917 = color['B']

if jhnah917 <= jhnan917:
    print('jhnan917')
else:
    print('jhnah917')