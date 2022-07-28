from sys import stdin
for _ in range(int(stdin.readline())):
    if int(stdin.readline()[-2]) % 2 == 0: print("even")
    else: print("odd")