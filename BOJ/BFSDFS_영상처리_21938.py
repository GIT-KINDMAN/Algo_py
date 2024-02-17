import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())
graph = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    line = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(0, len(line), 3):
        if j + 2 < len(line) and j // 3 < M:
            graph[i][j // 3] = (line[j] + line[j + 1] + line[j + 2]) // 3

T = int(sys.stdin.readline().rstrip())

q = deque()
visited = [[False for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if graph[i][j] < T:
            graph[i][j] = 0
        else:
            graph[i][j] = 1
            q.append((i, j))


def in_boundary(bi, bj):
    return 0 <= bi < N and 0 <= bj < M


def bfs(starti, startj, ans):

    # 우 하 좌 상
    di = [0,1,0,-1]
    dj = [1,0,-1,0]

    visited[starti][startj] = True
    dq = deque()
    dq.append((starti, startj))

    while dq:
        nowi, nowj = dq.popleft()

        for d in range(4):
            nexti, nextj = nowi+di[d], nowj+dj[d]
            if not in_boundary(nexti, nextj):
                continue
            if graph[nexti][nextj] == 1 and visited[nexti][nextj] == False:
                visited[nexti][nextj] = True
                dq.append((nexti, nextj))

    return ans+1


result = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and not visited[i][j]:
            result = bfs(i, j, result)

print(result)

