from sys import stdin

for _ in range(int(stdin.readline())):
    print('yes' if 6 <= len(stdin.readline().strip()) <= 9 else 'no')