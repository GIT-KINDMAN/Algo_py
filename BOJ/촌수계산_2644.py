import sys

# N, M, V = map(int, sys.stdin.readline().split())

N = int(input())
A, B = map(int, input().split())
way = int(input())

graph = [[] * (N + 1) for _ in range(N + 1)]
# result = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(way):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (N + 1)


def dfs(graph, v, B, visited, cnt):

    if visited[v]:
        return -1

    visited[v] = True

    if v == B:
        return cnt

    for i in graph[v]:
        result = dfs(graph, i, B, visited, cnt + 1)
        if result != -1:
            return result

    return -1


result = dfs(graph, A, B, visited, 0)
print(result)