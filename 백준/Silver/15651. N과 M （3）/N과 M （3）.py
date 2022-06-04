n, m = map(int, input().split())
visited = []

def dfs(k):
    if(len(visited) == m):
        print(' '.join(map(str, visited)))
    else:
        for i in range(1, n+1):
            visited.append(i)
            dfs(k+1)
            visited.pop()

dfs(1)