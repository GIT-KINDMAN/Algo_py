import sys
from collections import deque

q = deque()
flag = False

while True:
    line = sys.stdin.readline().rstrip()

    if line == '.':
        break

    flag = False
    q.clear()

    for j in line:
        if j == '(' or j == '{' or j == '[':
            q.append(j)
        elif j in ')}]':
            # if not q or (j ==q.pop() ==):
                flag = True
                break

    if flag or q:
        print("no")
    else:
        print("yes")