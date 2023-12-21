#  문제 구조가 구조물이 바닥에 디딘 벽의 형태라 1차원 적층으로 가능했음. 슈퍼마리오 식 공중 부양 블럭이었으면 2차원 델타 탐색을 시도해야 했을 것임

from collections import deque

N, M = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))

matrix = [[1 for _ in range(M)] for _ in range(N)]

for m in range(M):
    n = N-arr[m]
    for i in range(n):
        matrix[i][m] = 0

visited = [[False for _ in range(M)] for _ in range(N)]
dj = [-1, 1]

count = 0
for ii in range(N-1, -1, -1):
    for jj in range(M-1, -1, -1):
        if matrix[ii][jj] == 0 and not visited[ii][jj]:
            cnt = 0
            l = False
            r = False
            q = deque()

            q.append((ii, jj))
            visited[ii][jj] = True
            cnt += 1

            flag = False
            while q:

                nowi, nowj = q.popleft()

                for d in range(2):

                    if l and r:
                        break

                    nextj = nowj + dj[d]
                    if nextj < 0 or nextj >= M:
                        continue

                    if visited[nowi][nextj]:
                        continue

                    if matrix[nowi][nextj] == 1:
                        if d == 0:
                            l = True
                        elif d == 1:
                            r = True
                        continue

                    q.append((nowi, nextj))
                    visited[nowi][nextj] = True
                    cnt += 1

                if l and r:
                    count += cnt
                    break


print(count)