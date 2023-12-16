import sys

N, M, K = map(int, sys.stdin.readline().rstrip().split(" "))
arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))

arr.sort(reverse=True)

count = 0
sum = 0
for i in range(M):
    count += 1

    if count % K == 0:
        sum += arr[1]
    else:
        sum += arr[0]

print(sum)