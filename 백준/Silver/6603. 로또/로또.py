visited = []
visitor = []
n = 6
def dfs(k):
    if(len(visited) == n):
        print(" ".join(map(str, visited)))
    else:
        for i in visitor[k:]:
            if i in visited:
                continue
            visited.append(i)
            dfs(visitor.index(i)+1)
            visited.pop()

while 1:
    temp = list(map(int, input().split()))
    if (temp[0] == 0):
        exit(0)
    visitor = temp[1:]
    dfs(0)
    print()