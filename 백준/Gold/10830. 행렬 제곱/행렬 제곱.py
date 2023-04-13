"""
file name: 10830.py

create time: 2023-04-13 13:03
author: Tera Ha
e-mail: terra2007@naver.com
github: https://github.com/terra2007
"""
from sys import stdin

N, B = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]

def square(matrix1, matrix2):
    matrix = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                matrix[i][j] += matrix1[i][k] * matrix2[k][j]
            matrix[i][j] %= 1000

    return matrix

def pow(B, matrix):
    if B == 1: return matrix
    if B == 2: return square(matrix, matrix)
    else:
        temp = pow(B // 2, matrix)
        if B % 2: return square(square(temp, temp), matrix)
        else: return square(temp, temp)

result = pow(B, board)
for i in range(N):
    for j in range(N):
        print(result[i][j] % 1000, end=" ")
    print()