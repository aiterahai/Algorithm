"""
file name: 2263.py

create time: 2023-04-10 23:17
author: Tera Ha
e-mail: terra2007@naver.com
github: https://github.com/terra2007
"""
from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 5)

N = int(stdin.readline())
inorder = list(map(int, stdin.readline().split()))
postorder = list(map(int, stdin.readline().split()))

def preorder(inStart, inEnd, postStart, postEnd):
    if inStart > inEnd or postStart > postEnd: return

    root = postorder[postEnd]

    leftNode = inorder.index(root) - inStart
    rightNode = inEnd - inorder.index(root)

    print(root, end=" ")
    preorder(inStart, inStart + leftNode - 1, postStart, postStart + leftNode - 1)
    preorder(inEnd - rightNode + 1, inEnd, postEnd - rightNode, postEnd - 1)

preorder(0, N - 1, 0, N - 1)