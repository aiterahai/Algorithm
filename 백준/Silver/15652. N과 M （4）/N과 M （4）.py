n, m = map(int, input().split())
visited = []

def dfs(k):
    if(len(visited) == m):
        print(' '.join(map(str, visited)))
    else:
        for i in range(k, n+1):
            visited.append(i)
            dfs(i)
            visited.pop()

dfs(1)