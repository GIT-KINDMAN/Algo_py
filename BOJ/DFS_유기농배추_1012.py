import sys
sys.setrecursionlimit(10 ** 9)
from collections import deque

TC = int(sys.stdin.readline().rstrip())

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


def valid_boundary(i, j, N, M):
    return 0 <= i < N and 0 <= j < M


def dfs(v, graph):
    i, j = v[0], v[1]

    if not graph[i][j]:
        return

    graph[i][j] = False

    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]

        if not valid_boundary(ni, nj, len(graph), len(graph[0])):
            continue

        if graph[ni][nj]:
            dfs((ni, nj), graph)


for _ in range(TC):

    # [N][M], K양배추
    M, N, K = map(int, sys.stdin.readline().rstrip().split(" "))

    matrix = [[False for _ in range(M)] for _ in range(N)]

    q = deque()

    for _ in range(K):
        j, i = map(int, sys.stdin.readline().rstrip().split(" "))
        matrix[i][j] = True
        q.append((i, j))

    cnt = 0
    while q:
        nowi, nowj = q.popleft()
        if matrix[nowi][nowj]:
            dfs((nowi, nowj), matrix)
            cnt += 1

    print(cnt)