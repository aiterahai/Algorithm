"""
file name: 17144.py

create time: 2023-04-13 11:45
author: Tera Ha
e-mail: terra2007@naver.com
github: https://github.com/terra2007
"""
from sys import stdin
board = stdin.readline().rstrip()
stack = []
result = []

for i in board:
    if i.isalpha(): result.append(i)
    elif i == '(': stack.append(i)
    elif i == '*' or i == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'): result.append(stack.pop())
        stack.append(i)
    elif i == '+' or i == '-':
        while stack and stack[-1] != '(': result.append(stack.pop())
        stack.append(i)
    elif i == ')':
        while stack and stack[-1] != '(': result.append(stack.pop())
        stack.pop()

print("".join(result + stack[::-1]))