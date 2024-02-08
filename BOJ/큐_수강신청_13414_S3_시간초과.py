import sys
from collections import deque
K, L = map(int, sys.stdin.readline().rstrip().split())

dq = deque()
for _ in range(L):
    val = int(sys.stdin.readline().rstrip())
    if val in dq:
        dq.remove(val)
        dq.append(val)
    else:
        dq.append(val)

for _ in range(K):
    if not dq:
        break
    print(dq.popleft())