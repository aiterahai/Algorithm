from collections import Counter
from sys import stdin
n = int(stdin.readline())
arr = sorted([int(stdin.readline()) for i in range(n)])
count = Counter(arr).most_common()
print(round(sum(arr)/n))
print(arr[n//2])
if len(arr) > 1:
    if count[0][1] == count[1][1]: print(count[1][0])
    else: print(count[0][0])
else: print(count[0][0])
print(max(arr)-min(arr))