from sys import stdin

def func(n):
    if n == 0: return 0
    if n % 2 == 0: return func(n // 2)
    return 1 - func(n // 2)

print(func(int(stdin.readline()) - 1))