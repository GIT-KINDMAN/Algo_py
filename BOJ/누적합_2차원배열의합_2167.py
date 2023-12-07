import sys

N, M = map(int, sys.stdin.readline().rstrip().split(" "))
graph = [[0] * (M+1) for _ in range(N+1)]

for i in range(1, N+1):
    line = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    for j in range(1, M+1):
        graph[i][j] = graph[i-1][j] + graph[i][j-1] - graph[i-1][j-1] + line[j-1] # line은 인덱스 논리가 다르므로 j-1 해야 정상값

K = int(input())

for i in range(K):
    line = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    x1, y1, x2, y2 = [i for i in line]

    print(graph[x2][y2] - graph[x2][y1-1] - graph[x1-1][y2] + graph[x1-1][y1-1])