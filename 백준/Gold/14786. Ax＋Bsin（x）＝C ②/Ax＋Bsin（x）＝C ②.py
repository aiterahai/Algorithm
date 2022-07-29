from sys import stdin
from decimal import *
pi = Decimal("3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679")
def sin(x):
    x = x % (pi*2)
    u, d, result, sign = x, 1, Decimal(x), 1
    for i in range(2, 100, 2):
        u = u * x * x
        d = d * i * (i + 1)
        sign = sign * -1
        result += Decimal(u / d * sign)
    return result
A, B, C = map(int, stdin.readline().split())
start, end = Decimal(0), Decimal(1000000)
for i in range(1000):
    mid = Decimal((start + end) / 2)
    if Decimal(A*mid + B*sin(mid)) < Decimal(C): start = mid
    else: end = mid
print(mid)