# 골드 4
# 85%) 적합하게 잘 풀어놓고 왜 조합이 아니라 순열을 골랐는지 참... 순서 상관 없으니 조합 문제인데... 헷갈 ㄴ
# 95%) 처음부터 zero가 0인 경우 (꽉 차있는 경우) 예외처리 고려할 것

from itertools import combinations
from collections import deque

N, M = map(int, input().split())
matrix = [[0 for _ in range(N)] for _ in range(N)]

virus = []

for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        p = line[j]
        if p == 1:
            matrix[i][j] = -1  # 벽
        elif p == 2:
            virus.append((i, j))  # 바이러스 시작 위치

di = [-1, 1, 0, 0]  # 상하좌우
dj = [0, 0, -1, 1]  # 상하좌우


def in_boundary(bi, bj):
    return 0 <= bi < N and 0 <= bj < N


def bfs(in_copy_matrix, q, max_val):
    cnt = 0
    flag = False

    zero = sum(row.count(0) for row in in_copy_matrix)

    if zero == 0:
        return 0

    while q:
        size = len(q)

        for _ in range(size):
            nowi, nowj, v = q.popleft()

            if v > max_val:
                flag = True
                break

            for d in range(4):
                ni = nowi + di[d]
                nj = nowj + dj[d]

                if not in_boundary(ni, nj):
                    continue

                if in_copy_matrix[ni][nj] == 0:
                    in_copy_matrix[ni][nj] = 1
                    zero -= 1
                    q.append((ni, nj, v+1))

        cnt += 1

        if flag:
            break

        if zero == 0:
            break

    if flag:
        return float("inf")
    if zero != 0:
        return -1
    return cnt


comb = list(combinations(range(len(virus)), M))

ans = float("inf")
for i in range(len(comb)):
    # copy_matrix = copy.deepcopy(matrix)
    copy_matrix = [[matrix[i][j] for j in range(N)] for i in range(N)]
    q = deque()
    for j in range(M):
        idx = comb[i][j]
        q.append((virus[idx][0], virus[idx][1], 0))
        copy_matrix[virus[idx][0]][virus[idx][1]] = 1

    count = bfs(copy_matrix, q, ans)
    if count == -1:
        continue
    ans = min(ans, count)


if ans == float("inf"):
    print(-1)
else:
    print(ans)