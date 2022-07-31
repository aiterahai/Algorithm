from sys import stdin

N, result = int(stdin.readline()), ""
if not N: print(0); exit(0)
while N: N, result = (N // -2 + 1, "1" + result) if N % -2 else (N // -2, "0" + result)
print(result)