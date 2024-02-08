# deque 사용 시 시간초과. remove -> pop 등으로는 해결불가
# map(딕셔너리) 사용

import sys

K, L = map(int, sys.stdin.readline().rstrip().split())
d = {}

for i in range(L):
    d[sys.stdin.readline().rstrip()] = i

result = sorted(d.items(), key=lambda x: x[1])

if len(result) < K:
    K = len(result)

for i in range(K):
    print(result[i][0])
