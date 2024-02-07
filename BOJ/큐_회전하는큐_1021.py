from collections import deque
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

q = deque(range(1, N+1))
target = deque(map(int, sys.stdin.readline().rstrip().split())) # 입력 line 바로 deque에 넣으면 됨.

count = 0
while target:
    med = (len(q) - 1) // 2
    target_x = target.popleft()

    idx = q.index(target_x)
    if idx <= med:
        while q[0] != target_x:
            v = q.popleft()
            q.append(v)
            count += 1
    else:
        while q[0] != target_x:
            v = q.pop()
            q.appendleft(v)
            count += 1

    q.popleft()

print(count)