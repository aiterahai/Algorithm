"""
file name: 9252.py

create time: 2023-04-18 12:06
author: Tera Ha
e-mail: terra2007@naver.com
github: https://github.com/terra2007
"""
from sys import stdin

s1 = stdin.readline().rstrip()
s2 = stdin.readline().rstrip()
table = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        if s1[i - 1] == s2[j - 1]: table[i][j] = table[i - 1][j - 1] + 1
        else: table[i][j] = max(table[i - 1][j], table[i][j - 1])

cur = table[-1][-1]
result = []

print(cur)

x, y = len(table) - 1, len(table[0]) - 1
cur = table[-1][-1]
while cur:
    if table[x][y - 1] == table[x - 1][y] == cur - 1:
        result.append(s1[x - 1])
        x, y, cur = x - 1, y - 1, cur - 1
    else:
        if table[x - 1][y] > table[x][y - 1]: x -= 1
        else: y -= 1

print("".join(result)[::-1])