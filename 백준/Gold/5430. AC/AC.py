from collections import deque
from sys import stdin
for _ in range(int(stdin.readline())):
    error = 0
    reverse_cnt = 0
    p = stdin.readline()
    n = int(stdin.readline())
    arr = stdin.readline()
    if arr == "[]\n": arr = []
    else: arr = deque(map(int, arr[1:-2].split(',')))
    for __ in range(len(p)-1):
        if p[__] == "R":
            reverse_cnt += 1;
        else:
            if len(arr) == 0:
                error = 1
                break;
            else:
                if(reverse_cnt%2 == 0):
                    arr.popleft()
                else:
                    arr.pop()
    if(reverse_cnt%2 == 1):
        arr.reverse()
    if error: print("error")
    else:
        print("[", end="")
        for i in range(len(arr)):
            if i != len(arr)-1: print(str(arr[i])+",", end="")
            else: print(arr[i], end="")
        print("]")