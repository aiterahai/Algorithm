n, m = map(int, input().split())
visited = []

def dfs(k):
    if(len(visited) == m):
        print(' '.join(map(str, visited)))
    else:
        for i in range(k, n+1):
            if i in visited:
                continue
            visited.append(i)
            dfs(i+1)
            visited.pop()

dfs(1)