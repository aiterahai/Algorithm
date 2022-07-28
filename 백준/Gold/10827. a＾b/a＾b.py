from sys import stdin
from decimal import Decimal, getcontext

getcontext().prec = 10000
A, B = stdin.readline().split()
answer = f"{Decimal(A) ** int(B):.10000f}".rstrip("0").rstrip(".")
print(answer)