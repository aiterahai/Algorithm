from sys import stdin

total, xor = 0, 0
for _ in range(int(stdin.readline())):
    command = list(map(int, stdin.readline().split()))
    if command[0] == 1: total += command[1]; xor = xor ^ command[1]
    elif command[0] == 2: total -= command[1]; xor = xor ^ command[1]
    elif command[0] == 3: print(total)
    else: print(xor)