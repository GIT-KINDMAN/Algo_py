import sys

N, M = map(int, input().split(" "))


# N == M인 경우 경우의 수 1개 (오름차순 이므로)
if N == M:
    print(*[i for i in range(1, N+1)], sep=" ")
    sys.exit(0)

visited = [False] * (N+1)
arr = [0] * M


def dfs(depth, start):
    if depth == M:
        print(*arr, sep=" ", end="\n")
        return

    for i in range(start, N):
        if not visited[i]:
            visited[i] = True

            arr[depth] = i+1
            dfs(depth+1, i+1)

            visited[i] = False


dfs(0, 0)