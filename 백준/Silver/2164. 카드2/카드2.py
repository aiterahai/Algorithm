from collections import deque
arr = deque([i for i in range(1, int(input())+1)])
throw = True
while len(arr) != 1:
    if throw:
        arr.popleft()
        throw = not throw
    else:
        arr.append(arr.popleft())
        throw = not throw
print(arr[0])