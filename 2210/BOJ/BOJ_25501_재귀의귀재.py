import sys
input = sys.stdin.readline

def recursion(s, l, r):
    global ck
    ck += 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)


n = int(input())
for i in range(n):
    word = input().strip()
    ck = 0

    print(isPalindrome(word), ck)