from sys import stdin
from itertools import combinations_with_replacement
from collections import Counter

def key(A, B, C):
    count = 0
    sequence = [[A, B], [B, C], [C, A]]
    for x, y in sequence:
        for index in range(4):
            count += x[index] != y[index]
    return count

category = ["INTJ", "INTP", "ENTJ", "ENTP", "INFJ", "INFP", "ENFJ", "ENFP", "ISTJ", "ISFJ", "ESTJ", "ESFJ", "ISTP", "ISFP", "ESTP", "ESFP"]
category = sorted(list(combinations_with_replacement(category, 3)), key=lambda x: key(*x))

for _ in range(int(stdin.readline())):
    N = int(stdin.readline())
    board = Counter(stdin.readline().split())
    for value in category:
        if sum((Counter(value) & board).values()) == 3:
            print(key(*value))
            break
