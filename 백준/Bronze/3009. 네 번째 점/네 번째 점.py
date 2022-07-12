from collections import Counter
x, y = [], []
for i in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
print(Counter(x).most_common(2)[1][0], Counter(y).most_common(2)[1][0])