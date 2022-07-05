from math import lcm

for i in range(int(input())):
    a, b = map(int, input().split())
    print(lcm(a, b))