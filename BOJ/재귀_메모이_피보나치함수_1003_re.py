import sys

TC = int(input())
sys.setrecursionlimit(10**9)

def fibo(n, memo):
    if n == 0:
        return 1, 0
    elif n == 1:
        return 0, 1

    if memo[n] != (-1, -1):
        return memo[n]

    zero, one = fibo(n - 1, memo)
    zero += fibo(n - 2, memo)[0]
    one += fibo(n - 2, memo)[1]

    memo[n] = (zero, one)
    return memo[n]


for _ in range(TC):
    N = int(input())
    memo = [(-1, -1) for _ in range(N + 1)]

    ans = fibo(N, memo)
    print(ans[0], ans[1])