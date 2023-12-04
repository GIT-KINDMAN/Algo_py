import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())

graph = [[0] * M for _ in range(N)]

for i in range(N):
    graph[i] = list(map(int, sys.stdin.readline().rstrip()))

#     동 남  서  북
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
visited = [[False] * M for _ in range(N)]

# print()
# print(*visited, sep="\n")


def boundary(i, j):
    return 0 <= i < N and 0 <= j < M


def bfs(starti, startj):
    q = deque()
    q.append((starti, startj, 1))
    visited[starti][startj] = True

    while q:
        now = q.popleft()
        nowi = now[0]
        nowj = now[1]
        cnt = now[2]

        if nowi == N - 1 and nowj == M - 1:
            return cnt

        for d in range(4):
            nexti = nowi + di[d]
            nextj = nowj + dj[d]

            if not boundary(nexti, nextj):
                continue

            if graph[nexti][nextj] == 0 or visited[nexti][nextj]:
                continue

            q.append((nexti, nextj, cnt+1))
            visited[nexti][nextj] = True

    return -1


print(bfs(0, 0))
