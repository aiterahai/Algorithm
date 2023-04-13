"""
file name: 10830.py

create time: 2023-04-13 13:03
author: Tera Ha
e-mail: terra2007@naver.com
github: https://github.com/terra2007
"""
from sys import stdin

N = int(stdin.readline())

def square(matrix1, matrix2):
    matrix = [[0 for _ in range(2)] for _ in range(2)]

    for i in range(2):
        for j in range(2):
            for k in range(2):
                matrix[i][j] += matrix1[i][k] * matrix2[k][j]
            matrix[i][j] %= 1000000007

    return matrix

def pow(B, matrix):
    if B == 1: return matrix
    if B == 2: return square(matrix, matrix)
    else:
        temp = pow(B // 2, matrix)
        if B % 2: return square(square(temp, temp), matrix)
        else: return square(temp, temp)

board = [[1, 1], [1, 0]]
print(pow(N, board)[1][0])