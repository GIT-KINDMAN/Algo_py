import sys

N = int(input())

for tc in range(1, N + 1):
    words = sys.stdin.readline().rstrip().split(" ")

    print(f"Case #{tc}: {' '.join(words[::-1])}")
