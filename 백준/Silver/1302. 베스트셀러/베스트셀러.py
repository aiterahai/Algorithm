from sys import stdin
from collections import Counter
print(Counter(sorted([stdin.readline()[:-1] for i in range(int(stdin.readline()))])).most_common(1)[0][0])