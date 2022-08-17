'''
268ms
'''
import sys

a, b = map(int, sys.stdin.readline().split())
aset = set(map(int, sys.stdin.readline().split()))
bset = set(map(int, sys.stdin.readline().split()))

print(len(aset ^ bset))
'''
input()
a = list(input().split())
b = list(input().split())
print(2*len(set(a+b)) - (len(a)+len(b)))
훨씬 빠름 180ms
'''
