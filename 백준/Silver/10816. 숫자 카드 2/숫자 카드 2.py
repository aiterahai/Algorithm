from collections import Counter

input()
counted = Counter(map(int, input().split()))
input()
for i in map(int, input().split()):
    print(counted[i], end=" ")