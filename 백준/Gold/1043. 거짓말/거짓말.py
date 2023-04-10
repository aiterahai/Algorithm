"""
file name: 1043.py

create time: 2023-04-10 22:53
author: Tera Ha
e-mail: terra2007@naver.com
github: https://github.com/terra2007
"""
from sys import stdin

N, M = map(int, stdin.readline().split())
truth = set(list(map(int, stdin.readline().split()))[1:])
board = [set(list(map(int, stdin.readline().split()))[1:]) for _ in range(M)]
temp = 1
count = 0
for i in board:
    for j in truth:
        if j in i: count += 1
if count == 0:
    print(M)
    exit(0)
for _ in range(M):
    for party in board:
        for i in list(truth):
            if i in party:
                for j in list(party):
                    truth.add(j)


result = 0
for party in board:
    count = 0
    for i in list(truth):
        if i in party: break
        count += 1
    if count == len(truth): result += 1
print(result)