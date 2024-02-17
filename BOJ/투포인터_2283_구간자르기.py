import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
arr = [0 for _ in range(1000001)]

for _ in range(N):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    for i in range(start, end):
        arr[i] += 1

l, r, val = 0, 0, 0
flag = False
while 0 <= l <= r < 1000001:
    if val == K:
        flag = True
        break
    elif val < K:
        val += arr[r]
        r += 1
    else:
        val -= arr[l]
        l += 1

if flag:
    print(f"{l} {r}")
else:
    print(f"{0} {0}")
