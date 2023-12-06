import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().rstrip().split())

box = [[[0] * M for _ in range(N)] for _ in range(H)]

q = deque()
visited = [[[False] * M for _ in range(N)] for _ in range(H)]

for h in range(H):
    for n in range(N):
        line = list(map(int, sys.stdin.readline().rstrip().split(" ")))
        for m in range(M):
            box[h][n][m] = line[m]
            if line[m] == 1:
                q.append((h, n, m, 0))
                visited[h][n][m] = True


#    동  남  서  북 하  상
dh = [0, 0, 0, 0, -1, 1]
dn = [0, 1, 0, -1, 0, 0]
dm = [1, 0, -1, 0, 0, 0]


def boundary(h, n, m):
    return 0 <= h < H and 0 <= n < N and 0 <= m < M


def bfs(box, q, visited):

    while q:

            now = q.popleft()
            h = now[0]  # 층
            n = now[1]  # 행
            m = now[2]  # 열
            day = now[3]

            visited[h][n][m] = True

            for d in range(6):
                nexth = h + dh[d]
                nextn = n + dn[d]
                nextm = m + dm[d]

                if not boundary(nexth, nextn, nextm):
                    continue

                next_val = box[nexth][nextn][nextm]

                if next_val == -1 or visited[nexth][nextn][nextm]:
                    continue

                if next_val == 0:
                    box[nexth][nextn][nextm] = 1
                    q.append((nexth, nextn, nextm, day+1))
                    visited[nexth][nextn][nextm] = True

    if any(any(0 in row for row in matrix) for matrix in box):
        return -1

    return day


answer = bfs(box, q, visited)
if answer == -1:
    print(-1)
else:
    print(answer)