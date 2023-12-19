import sys
from itertools import combinations

sys.setrecursionlimit(10**9)

N, M = map(int, sys.stdin.readline().rstrip().split(" "))

matrix = [[0 for _ in range(N)] for _ in range(N)]

house = []
chicken = []

for i in range(N):
    line = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    matrix[i] = line

    if 1 in line:
        for j in range(N):
            if matrix[i][j] == 1:
                house.append((i, j))
    if 2 in line:
        for j in range(N):
            if matrix[i][j] == 2:
                chicken.append((i, j))


def distance(selected_chickens):
    total_dist = 0
    for h in house:
        dist_list = [abs(h[0] - c[0]) + abs(h[1] - c[1]) for c in selected_chickens]
        total_dist += min(dist_list)
    return total_dist


combination = combinations(chicken, M)

sum__ = float('inf')
for selected_chickens in combination:
    total_dist = distance(selected_chickens)
    sum__ = min(sum__, total_dist)

print(sum__)

# import sys
# from itertools import combinations
# sys.setrecursionlimit(10**9)
#
# N, M = map(int, sys.stdin.readline().rstrip().split(" "))
#
# matrix = [[0 for _ in range(N)] for _ in range(N)]
#
# house = []
# chicken = []
#
# for i in range(N):
#     line = list(map(int, sys.stdin.readline().rstrip().split(" ")))
#     matrix[i] = line
#
#     if 1 in line:
#         for j in range(N):
#             if matrix[i][j] == 1:
#                 house.append((i, j))
#     if 2 in line:
#         for j in range(N):
#             if matrix[i][j] == 2:
#                 chicken.append((i, j))
#
# # print(house)
# # print(chicken)
#
#
# def distance(i, j):
#     sum_ = 0
#     for k in range(len(house)):
#         a, b = house[k]
#         sum_ += abs(i-a) + abs(j-b)
#     return sum_
#
#
# combination = combinations([i for i in range(M)], M)
#
# sum__ = 10 ** 3
# for combi in combination:
#     index = list(combi)
#
#     cur = 10 ** 3
#     for i in index:
#         a, b = chicken[i]
#         data = distance(a, b)
#         cur = min(cur, data)
#
#     sum__ = min(sum__, cur)
#
#
# print(sum__)