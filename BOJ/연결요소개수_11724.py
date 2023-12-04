# 반성점)
# return이나 cnt 값으로 해결하려 하는건 파이썬에서 그닥 좋지 않은 것 같다.
# 당초의 아이디어 대로, for문 내에서 dfs를 돌리되 reallocated 없이 visited 선언 후 방문 체크해서 False인 node만 dfs 마저 돌리면 된다.
# 기록 할만한 점)
# sys.setrecursionlimit(10**5) 등을 사용하여 재귀 깊이를 늘려줘야 통과 가능했던 문제였다.

import sys
sys.setrecursionlimit(10 ** 5)

N, lines = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for i in range(lines):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (N + 1)

def dfs(v):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
           dfs(i)

count = 0
for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)