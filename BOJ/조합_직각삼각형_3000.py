from itertools import combinations
from itertools import permutations
import sys


def check(_c, cnt):
    edge = [_c[0], _c[1], _c[2]]
    perm = permutations(edge, 3)

    flag = False
    for p in perm:
        ax, ay, bx, by, cx, cy = p[0][0], p[0][1], p[1][0], p[1][1], p[2][0], p[2][1]
        if ax == bx and by == cy:
            flag = True
            break

    if flag:
        cnt += 1

    return cnt


N = int(sys.stdin.readline().rstrip())

arr = []
for i in range(N):
    X, Y = map(int, sys.stdin.readline().rstrip().split())
    arr.append((X, Y))

comb = combinations(arr, 3)

ans = 0
for c in comb:
    ans = check(c, ans)

print(ans)