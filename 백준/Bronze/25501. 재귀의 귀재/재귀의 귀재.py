from sys import stdin

def isPalindrome(s):
    return int(s == s[::-1])

def recursion(s):
    length = len(s)
    n = 1
    for i in range(length // 2):
        j = length - i - 1
        if s[i] == s[j]: n += 1
        else: break
    return n


N = int(stdin.readline())
for i in range(N):
    temp = stdin.readline().rstrip()
    print(isPalindrome(temp), recursion(temp))