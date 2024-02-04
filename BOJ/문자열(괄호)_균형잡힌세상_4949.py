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
        # elif (len(q) == 0) and (j == ')' or j == '}' or j == '}'):
        #     flag = True
        #     break
        elif j == ')':
            if not q:
                flag = True
                break
            if q.pop() != '(':
                flag = True
                break
        elif j == '}':
            if not q:
                flag = True
                break
            if q.pop() != '{':
                flag = True
                break
        elif j == ']':
            if not q:
                flag = True
                break
            if q.pop() != '[':
                flag = True
                break

    if flag or q:
        print("no")
    else:
        print("yes")