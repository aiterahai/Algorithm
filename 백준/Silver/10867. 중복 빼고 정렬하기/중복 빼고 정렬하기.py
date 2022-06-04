input()
arr = sorted(list(set(map(int, input().split()))))
for i in arr:
    print(i, end=" ")