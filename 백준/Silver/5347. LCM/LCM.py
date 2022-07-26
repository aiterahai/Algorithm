from math import lcm
from sys import stdin

for _ in range(int(stdin.readline())): print(lcm(*map(int, stdin.readline().split())))