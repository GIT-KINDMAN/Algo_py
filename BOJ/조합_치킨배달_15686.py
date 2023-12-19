import sys
sys.setrecursionlimit(10**9)

N, M = map(int, sys.stdin.readline().rstrip().split(" "))

matrix = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    matrix[i] = list(map(int, sys.stdin.readline().rstrip().split(" ")))
# matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

