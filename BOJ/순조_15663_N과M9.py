from itertools import permutations

N, M = map(int, input().split())
input_list = list(map(int, input().split()))

# arr = [list(p) for p in permutations(input_list, M)]
arr = sorted(set(permutations(input_list, M)))

for item in arr:
    print(*item)