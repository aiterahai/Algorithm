from sys import stdin
n = int(stdin.readline())
arr = [int(stdin.readline()) for _ in range(n)]
stack = []
result = []
count = 0
i = 1
while(count != len(arr)):
    if len(stack) == 0:
        stack.append(i)
        i += 1
        result.append("+")
    elif stack[-1] != arr[count]:
        stack.append(i)
        i += 1
        result.append("+")
    else:
        stack.pop()
        count += 1
        result.append("-")
    if (2 * n < len(result)):
        print("NO")
        exit(0)

for i in result:
        print(i)