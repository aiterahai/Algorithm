from sys import stdin
from collections import Counter

for _ in range(int(stdin.readline())):
    count = 1
    result = Counter([stdin.readline().split()[1] for i in range(int(stdin.readline()))]).values()
    for i in result: count *= i + 1
    print(count - 1)