import sys
from collections import deque

TC = 0
while True:
    TC += 1
    line = list(sys.stdin.readline().rstrip())

    if line[0] == '-':
        break

    q = deque()

    cnt = 0
    for i in range(len(line)):
        if line[i] == '{':
            q.append('{')
        elif line[i] == '}':
            if q:
                q.pop()
            elif not q:

