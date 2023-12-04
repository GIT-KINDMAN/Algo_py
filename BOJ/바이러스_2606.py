import sys

N = int(input())
way = int(input())

graph = [[] * (N+1) for _ in range(N+1)]

for _ in range(way):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    graph[x].append(y)
    graph[y].append(x)


visited = [False] * (N+1)

def dfs(v):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(i)


dfs(1)
print(visited.count(True)-1)