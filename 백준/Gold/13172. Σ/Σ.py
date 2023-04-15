"""
file name: 13172.py

create time: 2023-04-15 21:59
author: Tera Ha
e-mail: terra2007@naver.com
github: https://github.com/terra2007
"""
from sys import stdin

X = 1000000007

def power(value, exp):
    if exp == 1: return value % X
    if exp % 2: return value * power(value, exp - 1) % X
    split = power(value, exp // 2)
    return split * split % X

result = 0
for _ in range(int(stdin.readline())):
    N, S = map(int, stdin.readline().split())
    result += S * power(N, X - 2) % X

print(result % X)