import sys

N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    line = list(sys.stdin.readline().rstrip())

    if line[-1] == '(':
        print("NO")
        continue

    sum = 0
    flag = False
    for i in range(len(line)):
        if line[i] == '(':
            sum += 1
        elif line[i] == ')':
            sum -= 1
            if sum < 0:
                print("NO")
                flag = True
                break

    if flag:
        continue

    if sum == 0:
        print("YES")
    else:
        print("NO")
