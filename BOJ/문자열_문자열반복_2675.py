import sys

TC = int(input())

word = []
for _ in range(TC):
    N, line = list(sys.stdin.readline().rstrip().split(" "))
    word = []
    N = int(N)
    for i in range(len(line)):
        word.append([line[i] for _ in range(N)])

    result = ''.join([''.join(w) for w in word])  # 이거 기억해두자
    print(result)
    word = []