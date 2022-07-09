from sys import stdin

for i in range(int(stdin.readline())):
    print(sum(map(int, stdin.readline().split(','))))