import sys
from collections import deque
queue = deque()
N = int(sys.stdin.readline())
size = 0
for i in range(N):
    command = sys.stdin.readline().split()
    if(command[0] == "push"):
        queue.append(int(command[1]))
        size += 1
    elif(command[0] == "pop"):
        if(size == 0):
            print("-1")
        else:
            print(queue.popleft())
            size -= 1
    elif(command[0] == "size"):
        print(size)
    elif(command[0] == "empty"):
        if(size == 0):
            print("1")
        else:
            print("0")
    elif(command[0] == "front"):
        if(size == 0):
            print("-1")
        else:
            print(queue[0])
    elif(command[0] == "back"):
        if(size == 0):
            print("-1")
        else:
            print(queue[-1])