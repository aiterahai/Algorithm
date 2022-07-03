from sys import stdin
N = int(stdin.readline())
ex = stdin.readline()[:-1]
stack = []
board = []
for i in range(N):
    board.append(int(stdin.readline()))
for i in ex:
    if i == "*": stack.append(stack.pop() * stack.pop())
    elif i == "+": stack.append(stack.pop() + stack.pop())
    elif i == "/":
        a = stack.pop()
        b = stack.pop()
        stack.append(b / a)
    elif i == "-":
        a = stack.pop()
        b = stack.pop()
        stack.append(b - a)
    else: stack.append(board[ord(i)-65])
print(f'{stack.pop():.2f}')