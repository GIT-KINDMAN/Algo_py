# 70864kb, 1320ms
# 수도코드
# 델타: 하우상좌 % 4
# 0,0 시작
#
# cur = N^2
#
# while cur>0
#  if 델타+1 == out bound
#   turn
#  if 델타+1 == 0
#   cur -= 1
#   [][] = cur
#   if cur == M
#    ti, tj = i, j

N = int(input())
x = int(input())

cur = N**2

# 하 우 상 좌
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

d = 0

matrix = [[0 for _ in range(N)] for _ in range(N)]


def in_boundary(i, j):
    return 0 <= i < N and 0 <= j < N


target_i, target_j = 1, 1
matrix[0][0] = cur
i, j = 0, 0

while cur > 1:
    ni, nj = i+di[d], j+dj[d]

    if not in_boundary(ni, nj) or matrix[ni][nj] != 0: # 행렬 밖 or 이미 적힌 달팽이
        d = (d+1) % 4
        ni, nj = i+di[d], j+dj[d]

    if matrix[ni][nj] == 0:
        cur -= 1
        matrix[ni][nj] = cur
        i, j = ni, nj
        if cur == x:
            target_i, target_j = ni+1, nj+1

for row in matrix:
    print(*row)
print(target_i, target_j)