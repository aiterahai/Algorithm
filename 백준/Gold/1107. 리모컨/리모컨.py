"""
file name: 1107.py

create time: 2023-04-05 21:57
author: Tera Ha
e-mail: terra2007@naver.com
github: https://github.com/terra2007
"""
from sys import stdin

N = int(stdin.readline())
M = int(stdin.readline())
broke = set(map(int, stdin.readline().split())) if M else set()

final = abs(N - 100)

for i in range(1000001):
    i = str(i)
    if [1 for j in i if int(j) in broke]: continue
    final = min(final, abs(N - int(i)) + len(i))

print(final)